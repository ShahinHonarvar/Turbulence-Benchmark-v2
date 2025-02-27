def if_contains_anagrams(string_list):
    anagram_dict = {}
    for string in string_list:
        if len(string) >= 3 and string.isalpha():
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(string)
            else:
                anagram_dict[sorted_string] = [string]
    anagram_count = 0
    for key in anagram_dict:
        anagram_count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
        if anagram_count > 70:
            return False
    return True