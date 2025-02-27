def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for s in string_list:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if sorted_str in anagram_dict:
                count += anagram_dict[sorted_str]
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    return count >= 79