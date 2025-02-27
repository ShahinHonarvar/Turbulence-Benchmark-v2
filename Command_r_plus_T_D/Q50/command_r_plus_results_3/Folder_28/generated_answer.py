def if_contains_anagrams(words_list: list[str]) -> bool:
    anagram_count = 0
    words_set = {word.lower() for word in words_list}
    for word in words_set:
        sorted_word = ''.join(sorted(word))
        anagram_count += sum((1 for w in words_set if w.lower() != word and sorted(w.lower()) == sorted_word))
    return anagram_count >= 81