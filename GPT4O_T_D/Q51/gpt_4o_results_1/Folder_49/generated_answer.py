def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    anagram_pairs = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if are_anagrams(normalized_strings[i], normalized_strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 10:
                    return False
    return True