def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        if len(s_lower) < 3:
            continue
        s_sorted = ''.join(sorted(s_lower))
        if s_sorted in anagrams:
            anagrams[s_sorted] += 1
            count += anagrams[s_sorted]
        else:
            anagrams[s_sorted] = 1
    return count <= 15