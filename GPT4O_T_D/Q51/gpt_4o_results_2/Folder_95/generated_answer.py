def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    anagram_pairs = 0
    processed = set()
    for i in range(len(strings)):
        if len(strings[i]) < 3:
            continue
        s1 = strings[i].lower()
        for j in range(i + 1, len(strings)):
            if len(strings[j]) < 3:
                continue
            s2 = strings[j].lower()
            if (s1, s2) not in processed and is_anagram(s1, s2):
                anagram_pairs += 1
                processed.add((s1, s2))
                processed.add((s2, s1))
                if anagram_pairs > 6:
                    return False
    return True