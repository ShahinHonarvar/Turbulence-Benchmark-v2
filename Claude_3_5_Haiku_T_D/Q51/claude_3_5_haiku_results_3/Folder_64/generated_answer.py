def if_contains_anagrams(strings):

    def is_valid_string(s):
        return s.isalpha() and len(s) >= 3

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    valid_strings = [s for s in strings if is_valid_string(s)]
    anagram_pairs = 0
    for i in range(len(valid_strings)):
        for j in range(i + 1, len(valid_strings)):
            if normalize_string(valid_strings[i]) == normalize_string(valid_strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 59:
                    return False
    return True