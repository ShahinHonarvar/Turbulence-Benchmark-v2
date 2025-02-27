def if_contains_anagrams(lst):
    anagram_count = 0
    processed_words = set()
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3 and sorted_word not in processed_words:
            anagram_count += sum((1 for w in lst if w.lower() != word.lower() and sorted(w.lower()) == sorted_word))
            processed_words.add(sorted_word)
    return anagram_count >= 108