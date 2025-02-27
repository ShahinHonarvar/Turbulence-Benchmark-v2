def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s_lower = s.lower()
        s_sorted = ''.join(sorted(s_lower))
        if len(s_sorted) >= 3 and s_sorted.isalpha():
            count += anagrams.get(s_sorted, 0)
            anagrams[s_sorted] = anagrams.get(s_sorted, 0) + 1
    return count <= 401