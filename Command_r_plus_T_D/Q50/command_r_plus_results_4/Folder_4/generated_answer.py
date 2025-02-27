def if_contains_anagrams(words_list: list[str]) -> bool:
    anagram_count = 0
    normalized_words = [word.lower() for word in words_list]
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if len(normalized_words[i]) >= 3 and len(normalized_words[j]) >= 3:
                if sorted(normalized_words[i]) == sorted(normalized_words[j]):
                    anagram_count += 1
                    if anagram_count >= 42:
                        return True
    return False