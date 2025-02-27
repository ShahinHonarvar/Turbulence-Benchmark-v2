def if_contains_anagrams(str_list):
    str_list = [str.lower() for str in str_list]
    anagram_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) < 3:
            continue
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(word)
    return len(anagram_dict) <= 61