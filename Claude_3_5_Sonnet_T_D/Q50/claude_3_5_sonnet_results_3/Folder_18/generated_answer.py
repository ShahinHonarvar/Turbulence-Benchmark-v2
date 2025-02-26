def if_contains_anagrams(string_list):
    anagram_count = 0
    word_dict = {}
    for word in string_list:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in word_dict:
                word_dict[sorted_word].append(word)
            else:
                word_dict[sorted_word] = [word]
    for sorted_word, anagrams in word_dict.items():
        if len(anagrams) > 1:
            anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_count >= 106