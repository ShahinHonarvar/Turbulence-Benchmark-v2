def if_contains_anagrams(word_list):
    anagram_count = 0
    processed_words = set()
    for word in word_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3 and sorted_word not in processed_words:
            anagram_count += sum((1 for w in word_list if sorted_word == ''.join(sorted(w.lower()))))
            processed_words.add(sorted_word)
    return anagram_count >= 277