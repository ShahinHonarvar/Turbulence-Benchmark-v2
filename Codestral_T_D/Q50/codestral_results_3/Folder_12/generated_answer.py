def if_contains_anagrams(string_list):
    anagram_dict = {}
    for word in string_list:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    anagram_pairs = sum([len(lst) * (len(lst) - 1) // 2 for lst in anagram_dict.values()])
    return anagram_pairs >= 69