def if_contains_anagrams(words_list: list[str]) -> bool:
    anagram_count = 0
    processed_words = set()
    for word in words_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3 and sorted_word not in processed_words:
            anagram_count += sum((1 for w in words_list if sorted(w.lower()) == sorted_word))
            processed_words.add(sorted_word)
        if anagram_count >= 16:
            return True
    return False