def if_contains_anagrams(list_of_strings):
    anagrams = {}
    count = 0
    for s in list_of_strings:
        s_lower = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            if sorted_s in anagrams:
                anagrams[sorted_s] += 1
            else:
                anagrams[sorted_s] = 1
    for k in anagrams:
        count += anagrams[k] * (anagrams[k] - 1) // 2
    return count >= 21