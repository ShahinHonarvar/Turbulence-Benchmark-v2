def if_contains_anagrams(str_list):
    anagram_groups = {}
    for string in str_list:
        filtered_string = ''.join(sorted((c.lower() for c in string if c.isalpha() and len(c) >= 3)))
        if filtered_string in anagram_groups:
            anagram_groups[filtered_string].append(string)
        else:
            anagram_groups[filtered_string] = [string]
    if len(anagram_groups) <= 41:
        return True
    else:
        return False