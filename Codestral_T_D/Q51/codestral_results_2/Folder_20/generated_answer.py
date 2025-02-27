def if_contains_anagrams(str_list):
    anagram_dict = {}
    for string in str_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string] += 1
        else:
            anagram_dict[sorted_string] = 1
    count = 0
    for value in anagram_dict.values():
        count += value * (value - 1) // 2
        if count > 131:
            return False
    return True