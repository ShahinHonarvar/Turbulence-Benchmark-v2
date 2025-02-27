def if_contains_anagrams(strings):
    anagram_pairs = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if normalized_strings[i] == normalized_strings[j]:
                anagram_pairs += 1
                if anagram_pairs > 210:
                    return False
    return True