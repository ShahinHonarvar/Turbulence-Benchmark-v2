def if_contains_anagrams(str_list):
    anagram_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(word)
    return len(anagram_dict) <= 66