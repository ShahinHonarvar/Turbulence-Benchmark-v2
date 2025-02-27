def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for string in string_list:
        lower_string = string.lower()
        sorted_string = ''.join(sorted(lower_string))
        if len(sorted_string) >= 3 and sorted_string.isalpha():
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(lower_string)
            else:
                anagram_dict[sorted_string] = [lower_string]
    for key in anagram_dict:
        value = anagram_dict[key]
        count += len(value) * (len(value) - 1) // 2
        if count > 464:
            return False
    return True