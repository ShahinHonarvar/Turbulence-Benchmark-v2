def if_contains_anagrams(words):
    normalized_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    anagram_count = 0
    used_indices = set()
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if normalized_words[i] == normalized_words[j] and (i, j) not in used_indices:
                anagram_count += 1
                used_indices.add((i, j))
                if anagram_count >= 4:
                    return True
    return False