def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    normalized_strings = [''.join(filter(str.isalpha, s)).lower() for s in strings]
    found_pairs = 0
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if len(normalized_strings[i]) >= 3 and len(normalized_strings[j]) >= 3:
                if is_anagram(normalized_strings[i], normalized_strings[j]):
                    found_pairs += 1
                    if found_pairs > 44:
                        return False
    return True