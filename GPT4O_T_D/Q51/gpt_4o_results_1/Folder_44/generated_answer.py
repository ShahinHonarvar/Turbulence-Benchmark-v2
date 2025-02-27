def if_contains_anagrams(strings):
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_count = 0
    checked_pairs = set()
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if (i, j) not in checked_pairs and normalized_strings[i] == normalized_strings[j]:
                anagram_count += 1
                if anagram_count > 75:
                    return False
                checked_pairs.add((i, j))
    return anagram_count <= 75