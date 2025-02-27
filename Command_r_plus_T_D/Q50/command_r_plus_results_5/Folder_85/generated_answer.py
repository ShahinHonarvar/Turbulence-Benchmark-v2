def if_contains_anagrams(word_list: list[str]) -> bool:
    anagram_count = 0
    word_set = {word.lower() for word in word_list}
    for word in word_set:
        sorted_word = ''.join(sorted(word))
        anagram_count += sum((1 for w in word_set if w != word and sorted(w) == sorted_word))
    return anagram_count >= 73