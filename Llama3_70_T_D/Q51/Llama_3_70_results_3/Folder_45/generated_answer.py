def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s_lower = ''.join(filter(str.isalpha, s.lower()))
        if len(s_lower) < 3:
            continue
        sorted_str = ''.join(sorted(s_lower))
        if sorted_str in anagrams:
            count += anagrams[sorted_str]
            anagrams[sorted_str] += 1
        else:
            anagrams[sorted_str] = 1
    return count <= 464