def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for string in strings:
        string_lower = string.lower()
        sorted_string = ''.join(sorted(string_lower))
        if len(string_lower) < 3:
            continue
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string] += 1
            count += anagram_dict[sorted_string]
            if count >= 3:
                return True
        else:
            anagram_dict[sorted_string] = 1
    return False