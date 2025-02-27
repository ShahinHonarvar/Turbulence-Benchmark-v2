def if_contains_anagrams(string_list):

    def sort_string(string):
        return ''.join(sorted(string))
    anagrams_dict = {}
    for string in string_list:
        if len(string) >= 3:
            sorted_string = sort_string(string.lower())
            if sorted_string in anagrams_dict:
                anagrams_dict[sorted_string].append(string)
            else:
                anagrams_dict[sorted_string] = [string]
    count = sum((len(value) // 2 for value in anagrams_dict.values()))
    return count >= 7