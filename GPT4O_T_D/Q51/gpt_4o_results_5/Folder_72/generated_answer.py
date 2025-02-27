def if_contains_anagrams(word_list):
    word_dict = {}
    num_pairs = 0
    for word in word_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in word_dict:
                word_dict[sorted_word] += 1
            else:
                word_dict[sorted_word] = 1
    for count in word_dict.values():
        num_pairs += count * (count - 1) // 2
        if num_pairs > 188:
            return False
    return True