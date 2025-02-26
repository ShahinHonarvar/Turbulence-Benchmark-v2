def if_contains_anagrams(strings):

    def is_valid_anagram(s1, s2):
        if len(s1) < 3 or len(s2) < 3:
            return False
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_valid_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 77:
                    return False
    return True