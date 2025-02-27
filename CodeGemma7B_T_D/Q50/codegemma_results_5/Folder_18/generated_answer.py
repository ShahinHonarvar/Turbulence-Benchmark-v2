def if_contains_anagrams(str_list):
    anagrams_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3 and sorted_word not in anagrams_dict:
            anagrams_dict[sorted_word] = [word]
        elif sorted_word in anagrams_dict:
            anagrams_dict[sorted_word].append(word)
    pair_count = 0
    for anagram_list in anagrams_dict.values():
        pair_count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return pair_count >= 106