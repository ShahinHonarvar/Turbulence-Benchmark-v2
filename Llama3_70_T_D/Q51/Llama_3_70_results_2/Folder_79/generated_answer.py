def if_contains_anagrams(str_list):
    anagrams_dict = {}
    anagram_pairs = set()
    for string in str_list:
        string_lower = string.lower()
        string_filtered = ''.join(filter(str.isalpha, string_lower))
        if len(string_filtered) < 3:
            continue
        sorted_string = ''.join(sorted(string_filtered))
        if sorted_string in anagrams_dict:
            anagrams_dict[sorted_string].append(string)
        else:
            anagrams_dict[sorted_string] = [string]
    for anagram_list in anagrams_dict.values():
        if len(anagram_list) > 1:
            for i in range(len(anagram_list)):
                for j in range(i + 1, len(anagram_list)):
                    anagram_pairs.add((anagram_list[i], anagram_list[j]))
    return len(anagram_pairs) <= 173