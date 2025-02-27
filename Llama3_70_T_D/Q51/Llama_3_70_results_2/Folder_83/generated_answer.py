def if_contains_anagrams(lst):
    anagram_count = 0
    seen = set()
    for s in lst:
        s_lower = ''.join(sorted(filter(str.isalpha, s.lower())))
        if len(s_lower) >= 3 and s_lower in seen:
            anagram_count += 1
        seen.add(s_lower)
    return anagram_count <= 19