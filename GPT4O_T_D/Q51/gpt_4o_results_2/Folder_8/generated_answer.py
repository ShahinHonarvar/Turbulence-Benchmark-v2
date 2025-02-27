def if_contains_anagrams(strings):
    anagram_count = 0
    checked_pairs = set()
    lower_strings = [s.lower() for s in strings]
    for i, word1 in enumerate(lower_strings):
        for j in range(i + 1, len(lower_strings)):
            word2 = lower_strings[j]
            if (word1, word2) not in checked_pairs and (word2, word1) not in checked_pairs:
                if len(word1) >= 3 and len(word2) >= 3 and (sorted(word1) == sorted(word2)):
                    anagram_count += 1
                checked_pairs.add((word1, word2))
                if anagram_count > 68:
                    return False
    return True