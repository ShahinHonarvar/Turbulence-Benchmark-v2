def if_contains_anagrams(strings):

    def is_valid_string(s):
        return all((c.isalpha() for c in s))

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    valid_strings = [s for s in strings if is_valid_string(s) and len(s) >= 3]
    anagram_count = 0
    checked = set()
    for i in range(len(valid_strings)):
        for j in range(i + 1, len(valid_strings)):
            if normalize_string(valid_strings[i]) == normalize_string(valid_strings[j]):
                anagram_pair = tuple(sorted([valid_strings[i], valid_strings[j]]))
                if anagram_pair not in checked:
                    anagram_count += 1
                    checked.add(anagram_pair)
                if anagram_count > 50:
                    return False
    return True