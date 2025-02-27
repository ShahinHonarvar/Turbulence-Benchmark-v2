def if_contains_anagrams(words_list: list[str]) -> bool:
    anagram_count = 0
    normalized_words = [''.join(sorted(word.lower())) for word in words_list]
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if normalized_words[i] == normalized_words[j] and len(normalized_words[i]) >= 3:
                anagram_count += 1
                if anagram_count > 77:
                    return False
    return True