def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        if not s.isalpha():
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            count += len(anagrams[sorted_s])
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    return count <= 93