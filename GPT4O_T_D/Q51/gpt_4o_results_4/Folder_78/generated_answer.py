def if_contains_anagrams(strings):
    anagram_count = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    for i, word1 in enumerate(normalized_strings):
        for word2 in normalized_strings[i + 1:]:
            if word1 == word2:
                anagram_count += 1
                if anagram_count > 70:
                    return False
    return True