def if_contains_anagrams(strings):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    valid_strings = [s for s in strings if len(s) >= 3]
    normalized_strings = [normalize_string(s) for s in valid_strings]
    anagram_pairs = 0
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if normalized_strings[i] == normalized_strings[j]:
                anagram_pairs += 1
                if anagram_pairs > 15:
                    return False
    return True