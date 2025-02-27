def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    count = 0
    for value in anagram_dict.values():
        count += value * (value - 1) // 2
        if count > 73:
            return False
    return True