def if_contains_anagrams(lst):
    anagram_dict = {}
    for string in lst:
        string_lower = string.lower()
        if len(string_lower) < 3:
            continue
        sorted_string = ''.join(sorted(string_lower))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(string_lower)
        else:
            anagram_dict[sorted_string] = [string_lower]
    anagram_count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            anagram_count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
        if anagram_count > 8:
            return True
    return False