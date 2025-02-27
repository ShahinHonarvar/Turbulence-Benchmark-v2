def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    valid_strings = [s for s in strings if len(s) >= 3]
    normalized = [sorted_chars(s) for s in valid_strings]
    anagram_count = 0
    for i in range(len(normalized)):
        for j in range(i + 1, len(normalized)):
            if normalized[i] == normalized[j]:
                anagram_count += 1
                if anagram_count > 81:
                    return False
    return True