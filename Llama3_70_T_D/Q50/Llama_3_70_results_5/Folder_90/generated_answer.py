def if_contains_anagrams(strings):
    anagram_pairs = set()
    for s1 in strings:
        for s2 in strings:
            if s1.lower() != s2.lower() and len(s1) >= 3 and (len(s2) >= 3):
                s1_sorted = ''.join(sorted(s1.lower()))
                s2_sorted = ''.join(sorted(s2.lower()))
                if s1_sorted == s2_sorted:
                    pair = tuple(sorted([s1, s2]))
                    anagram_pairs.add(pair)
    return len(anagram_pairs) >= 177