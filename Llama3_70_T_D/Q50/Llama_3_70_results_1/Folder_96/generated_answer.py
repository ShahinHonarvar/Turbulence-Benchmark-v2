def if_contains_anagrams(lst):
    lst = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    seen = set()
    anagram_count = 0
    for s in lst:
        if s in seen:
            anagram_count += 1
        seen.add(s)
    return anagram_count >= 98