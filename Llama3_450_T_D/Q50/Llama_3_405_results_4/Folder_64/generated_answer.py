def if_contains_anagrams(string_list):
    anagram_dict = {}
    anagram_count = 0
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(string)
            else:
                anagram_dict[sorted_string] = [string]
    for key, value in anagram_dict.items():
        if len(value) > 1:
            anagram_count += len(value) * (len(value) - 1) // 2
            if anagram_count >= 5:
                return True
    return False