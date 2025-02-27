def if_contains_anagrams(words):
    normalized_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    anagram_pairs_count = sum((normalized_words.count(word) - 1 for word in set(normalized_words))) // 2
    return anagram_pairs_count <= 64