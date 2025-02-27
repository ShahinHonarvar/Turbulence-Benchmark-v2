def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    normalized_strings = [s.lower() for s in strings if len(s) >= 3]
    anagram_pairs = 0
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if is_anagram(normalized_strings[i], normalized_strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 58:
                    return False
    return True