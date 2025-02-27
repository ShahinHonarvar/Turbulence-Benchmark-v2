def if_contains_anagrams(str_list):
    unprocessed_list = []
    for word in str_list:
        new_word = ''.join(sorted(word.lower()))
        if len(new_word) >= 3:
            unprocessed_list.append(new_word)
    anagram_dict = {}
    for word in unprocessed_list:
        if word not in anagram_dict:
            anagram_dict[word] = []
        anagram_dict[word].append(word)
    return len(anagram_dict) <= 92