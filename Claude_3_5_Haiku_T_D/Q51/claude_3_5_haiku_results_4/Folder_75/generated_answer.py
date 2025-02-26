def if_contains_anagrams(strings):

    def is_valid_string(s):
        return s.isalpha()

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    valid_strings = [s for s in strings if is_valid_string(s)]
    norm_strings = [normalize_string(s) for s in valid_strings]
    anagram_count = 0
    seen_norms = set()
    for norm in norm_strings:
        if len(norm) >= 3:
            if norm in seen_norms:
                anagram_count += 1
                if anagram_count > 55:
                    return False
            seen_norms.add(norm)
    return True