def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for string in strings:
        string = string.lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(string)
        else:
            anagram_dict[sorted_string] = [string]
    for anagram_group in anagram_dict.values():
        if len(anagram_group) >= 2:
            anagram_count += len(anagram_group) * (len(anagram_group) - 1) // 2
    return anagram_count >= 14