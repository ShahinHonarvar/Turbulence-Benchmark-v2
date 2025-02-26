def if_contains_anagrams(string_list):
    anagram_dict = {}
    anagram_count = 0
    for string in string_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(string)
            if len(anagram_dict[sorted_string]) == 2:
                anagram_count += 1
                if anagram_count == 2:
                    return True
        else:
            anagram_dict[sorted_string] = [string]
    return False