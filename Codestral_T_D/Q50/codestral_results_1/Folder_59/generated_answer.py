def if_contains_anagrams(string_list):
    anagram_dict = {}
    for string in string_list:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            sorted_string = ''.join(sorted(lower_string))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(lower_string)
            else:
                anagram_dict[sorted_string] = [lower_string]
    anagram_count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2:
            anagram_count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
            if anagram_count >= 10:
                return True
    return False