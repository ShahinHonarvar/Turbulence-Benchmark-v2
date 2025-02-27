def if_contains_anagrams(words):
    normalized_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    anagram_count = 0
    checked_indices = set()
    for i in range(len(normalized_words)):
        if i in checked_indices:
            continue
        for j in range(i + 1, len(normalized_words)):
            if normalized_words[i] == normalized_words[j]:
                anagram_count += 1
                checked_indices.add(j)
                if anagram_count >= 40:
                    return True
    return False