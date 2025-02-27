def if_contains_anagrams(str_list):
    anagram_groups = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower().replace(' ', '')))
        if len(sorted_string) >= 3 and sorted_string not in anagram_groups:
            anagram_groups[sorted_string] = [string]
        elif len(sorted_string) >= 3:
            anagram_groups[sorted_string].append(string)
    return len(anagram_groups) <= 97