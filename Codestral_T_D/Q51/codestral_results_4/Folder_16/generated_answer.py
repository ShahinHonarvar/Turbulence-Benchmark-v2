def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) < 3:
            continue
        sorted_string = ''.join(sorted(lower_string))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(lower_string)
        else:
            anagram_dict[sorted_string] = [lower_string]
    anagram_pairs = 0
    for anagram_list in anagram_dict.values():
        if len(anagram_list) > 1:
            anagram_pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
            if anagram_pairs > 24:
                return False
    return True