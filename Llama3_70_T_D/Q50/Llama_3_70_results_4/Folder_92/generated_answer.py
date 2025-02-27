def if_contains_anagrams(lst):
    anagram_dict = {}
    for string in lst:
        string_lower = string.lower()
        if len(string_lower) < 3:
            continue
        sorted_string = ''.join(sorted(string_lower))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(string)
        else:
            anagram_dict[sorted_string] = [string]
    count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            count += 1
            if count >= 2:
                return True
    return False