def if_contains_anagrams(lst):
    anagram_count = 0
    seen = set()
    for s in lst:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in seen:
            anagram_count += 1
        seen.add(sorted_s)
    return anagram_count >= 26