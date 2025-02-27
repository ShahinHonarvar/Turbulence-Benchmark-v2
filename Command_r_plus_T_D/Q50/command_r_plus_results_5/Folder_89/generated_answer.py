def if_contains_anagrams(words_list: list[str]) -> bool:
    anagram_count = 0
    anagram_dict = {}
    for word in words_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    for anagram_group in anagram_dict.values():
        if len(anagram_group) >= 2 and all((len(word) >= 3 for word in anagram_group)):
            anagram_count += len(anagram_group)
            if anagram_count >= 36:
                return True
    return False