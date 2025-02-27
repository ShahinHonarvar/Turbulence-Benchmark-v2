def if_contains_anagrams(str_list):
    anagram_pairs = 0
    anagram_dict = {}
    for word in str_list:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            anagram_pairs += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
            if anagram_pairs > 58:
                return False
    return True