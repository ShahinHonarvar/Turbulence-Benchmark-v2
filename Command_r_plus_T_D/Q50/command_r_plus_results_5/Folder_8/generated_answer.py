def if_contains_anagrams(words_list: list[str]) -> bool:
    anagram_count = 0
    word_dict = {}
    for word in words_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in word_dict:
                anagram_count += 1
            else:
                word_dict[sorted_word] = word
    return anagram_count >= 85