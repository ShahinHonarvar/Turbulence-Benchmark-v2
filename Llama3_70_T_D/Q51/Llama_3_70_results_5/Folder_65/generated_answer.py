def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        if len(s) < 3:
            continue
        s = ''.join(filter(str.isalpha, s)).lower()
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    for k in anagrams:
        count += len(anagrams[k]) * (len(anagrams[k]) - 1) // 2
        if count > 72:
            break
    return count <= 72