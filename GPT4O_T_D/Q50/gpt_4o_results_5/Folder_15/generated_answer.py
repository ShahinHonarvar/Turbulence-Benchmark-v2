def if_contains_anagrams(words):
    anagram_count = 0
    normalized_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    seen_pairs = set()
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if normalized_words[i] == normalized_words[j] and (i, j) not in seen_pairs:
                anagram_count += 1
                seen_pairs.add((i, j))
                if anagram_count >= 4:
                    return True
    return False