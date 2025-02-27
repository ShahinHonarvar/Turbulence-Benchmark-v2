def if_contains_anagrams(lst):
    anagram_count = 0
    processed_words = set()
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in processed_words:
            anagram_count += 1
        else:
            processed_words.add(sorted_word)
    return anagram_count >= 3