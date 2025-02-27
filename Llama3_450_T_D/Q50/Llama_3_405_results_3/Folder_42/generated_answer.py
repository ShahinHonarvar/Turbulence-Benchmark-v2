def if_contains_anagrams(str_list):
    anagram_dict = {}
    anagram_count = 0
    for string in str_list:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            sorted_string = ''.join(sorted(lower_string))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string] += 1
            else:
                anagram_dict[sorted_string] = 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 233