def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for s in string_list:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3 and sorted_str.isalpha():
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    for k in anagram_dict:
        if anagram_dict[k] > 1:
            count += anagram_dict[k] * (anagram_dict[k] - 1) // 2
        if count > 30:
            return False
    return True