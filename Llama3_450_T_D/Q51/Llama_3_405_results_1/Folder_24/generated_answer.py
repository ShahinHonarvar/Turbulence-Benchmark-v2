def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for string in string_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(string) >= 3 and sorted_str.isalpha():
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(string)
            else:
                anagram_dict[sorted_str] = [string]
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
            if count > 96:
                return False
    return True