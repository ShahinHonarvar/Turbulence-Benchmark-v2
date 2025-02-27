def if_contains_anagrams(str_list):
    anagram_dict = {}
    for word in str_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = [word]
            else:
                anagram_dict[sorted_word].append(word)
    count = 0
    for anagram_list in anagram_dict.values():
        count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return count >= 88