def if_contains_anagrams(strings):

    def is_valid_string(s):
        return all((c.isalpha() for c in s))

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    valid_strings = [s for s in strings if is_valid_string(s) and len(s) >= 3]
    anagram_count = 0
    for i in range(len(valid_strings)):
        for j in range(i + 1, len(valid_strings)):
            if sorted_string(valid_strings[i]) == sorted_string(valid_strings[j]):
                anagram_count += 1
                if anagram_count > 21:
                    return False
    return True