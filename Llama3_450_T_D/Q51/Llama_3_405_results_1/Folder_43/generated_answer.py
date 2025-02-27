def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            if len(anagrams[sorted_s]) == 1:
                count += 1
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    return count <= 3