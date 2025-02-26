def if_contains_anagrams(strings):

    def is_valid_string(s):
        return all((c.isalpha() and c.islower() for c in s))

    def canonicalize(s):
        return ''.join(sorted(s.lower()))
    valid_strings = [s for s in strings if is_valid_string(s) and len(s) >= 3]
    anagram_pairs = 0
    for i in range(len(valid_strings)):
        for j in range(i + 1, len(valid_strings)):
            if canonicalize(valid_strings[i]) == canonicalize(valid_strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 445:
                    return False
    return True