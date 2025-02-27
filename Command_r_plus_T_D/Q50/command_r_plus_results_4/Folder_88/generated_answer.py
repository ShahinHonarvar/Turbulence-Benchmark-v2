def if_contains_anagrams(words_list: list[str]) -> bool:
    count = 0
    anagram_dict = {}
    for word in words_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) < 3:
            continue
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    for anagram_list in anagram_dict.values():
        if len(anagram_list) > 1:
            count += len(anagram_list) * (len(anagram_list) - 1)
    return count >= 34