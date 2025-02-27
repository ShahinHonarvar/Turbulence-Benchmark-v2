def if_contains_anagrams(word_list):
    word_dict = {}
    for word in word_list:
        word = word.lower()
        if len(word) >= 3 and word.isalpha():
            sorted_word = ''.join(sorted(word))
            if sorted_word in word_dict:
                word_dict[sorted_word] += 1
            else:
                word_dict[sorted_word] = 1
    count = 0
    for key in word_dict.values():
        count += key * (key - 1) // 2
    return count <= 75