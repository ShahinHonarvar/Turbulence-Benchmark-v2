def if_contains_anagrams(lst):
    anagram_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            s1 = ''.join(sorted(lst[i].lower()))
            s2 = ''.join(sorted(lst[j].lower()))
            if len(s1) >= 3 and len(s2) >= 3 and (s1 == s2):
                anagram_pairs.add(tuple(sorted([lst[i].lower(), lst[j].lower()])))
    return len(anagram_pairs) >= 36