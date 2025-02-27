def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    normalized_strings = [normalize(s) for s in strings if len(s) >= 3]
    anagram_pairs = 0
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if normalized_strings[i] == normalized_strings[j]:
                anagram_pairs += 1
                if anagram_pairs > 46:
                    return False
    return True