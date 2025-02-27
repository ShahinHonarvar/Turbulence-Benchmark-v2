def if_contains_anagrams(strings):
    anagram_count = 0
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
    for anagram_list in anagram_dict.values():
        if len(anagram_list) > 1:
            anagram_count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return anagram_count <= 206