def if_contains_anagrams(lst):
    anagram_count = 0
    anagrams_dict = {}
    for string in lst:
        string_lower = string.lower()
        sorted_string = ''.join(sorted(string_lower))
        if len(string_lower) >= 3:
            if sorted_string in anagrams_dict:
                anagram_count += anagrams_dict[sorted_string]
                anagrams_dict[sorted_string] += 1
            else:
                anagrams_dict[sorted_string] = 1
    return anagram_count <= 60