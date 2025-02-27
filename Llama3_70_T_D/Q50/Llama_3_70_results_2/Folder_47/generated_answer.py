def if_contains_anagrams(strings):
    anagram_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            s1 = ''.join(sorted(strings[i].lower()))
            s2 = ''.join(sorted(strings[j].lower()))
            if len(s1) >= 3 and len(s2) >= 3 and (s1 == s2):
                anagram_pairs.add(tuple(sorted([strings[i], strings[j]])))
    return len(anagram_pairs) >= 47