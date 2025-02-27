def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs_count = 0
    normalized_strings = [normalize(s) for s in strings if len(s) >= 3]
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if normalized_strings[i] == normalized_strings[j]:
                anagram_pairs_count += 1
                if anagram_pairs_count > 6:
                    return False
    return True