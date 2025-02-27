def if_contains_anagrams(words):
    anagram_pairs = 0
    normalized_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if normalized_words[i] == normalized_words[j]:
                anagram_pairs += 1
                if anagram_pairs >= 98:
                    return True
    return False