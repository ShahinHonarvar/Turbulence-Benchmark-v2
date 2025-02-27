def if_contains_anagrams(words):
    anagram_count = 0
    normalized_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    n = len(normalized_words)
    for i in range(n):
        for j in range(i + 1, n):
            if normalized_words[i] == normalized_words[j]:
                anagram_count += 1
                if anagram_count >= 59:
                    return True
    return False