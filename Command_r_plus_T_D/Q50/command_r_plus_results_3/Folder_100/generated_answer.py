def if_contains_anagrams(words_list: list[str]) -> bool:
    anagram_count = 0
    word_dict = {}
    for word in words_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in word_dict:
            word_dict[sorted_word].append(word)
        else:
            word_dict[sorted_word] = [word]
    for anagram_group in word_dict.values():
        if len(anagram_group) >= 2 and len(anagram_group[0]) >= 3:
            anagram_count += len(anagram_group) * (len(anagram_group) - 1)
    return anagram_count >= 95