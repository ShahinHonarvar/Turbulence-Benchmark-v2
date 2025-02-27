def if_contains_anagrams(strings):

    def is_valid_anagram_pair(s1, s2):
        return len(s1) >= 3 and len(s2) >= 3 and (sorted(s1) == sorted(s2))
    strings = [s.lower() for s in strings]
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_valid_anagram_pair(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 14:
                    return False
    return True