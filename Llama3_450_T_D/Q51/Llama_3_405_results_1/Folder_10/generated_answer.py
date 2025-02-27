def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for s in string_list:
        s = ''.join(filter(str.isalpha, s)).lower()
        sorted_str = ''.join(sorted(s))
        if len(s) >= 3:
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(s)
            else:
                anagram_dict[sorted_str] = [s]
    for k in anagram_dict:
        if len(anagram_dict[k]) > 1:
            count += len(anagram_dict[k]) * (len(anagram_dict[k]) - 1) // 2
        if count > 21:
            return False
    return True