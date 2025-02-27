def if_contains_anagrams(string_list):
    anagram_dict = {}
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(string)
            else:
                anagram_dict[sorted_string] = [string]
    count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            count += 1
        if count >= 4:
            return True
    return False