def if_contains_anagrams(words_list):
    anagram_count = 0
    word_dict = {}
    for word in words_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) < 3:
            continue
        if sorted_word in word_dict:
            word_dict[sorted_word].append(word)
        else:
            word_dict[sorted_word] = [word]
    for anagram_group in word_dict.values():
        if len(anagram_group) >= 2:
            anagram_count += 1
    return anagram_count >= 97