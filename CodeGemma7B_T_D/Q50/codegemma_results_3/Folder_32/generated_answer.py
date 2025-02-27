def if_contains_anagrams(str_list):
    anagram_dict = {}
    pairs_cnt = 0
    for word in str_list:
        word = ''.join(sorted(word.lower()))
        if word not in anagram_dict:
            anagram_dict[word] = 1
        else:
            pairs_cnt += anagram_dict[word] + 1
            anagram_dict[word] += 1
    if pairs_cnt >= 194:
        return True
    else:
        return False