def if_contains_anagrams(strings):
    anagram_dict = {}
    anagram_count = 0
    for string in strings:
        string_lower = string.lower()
        sorted_string = ''.join(sorted(filter(str.isalpha, string_lower)))
        if len(sorted_string) < 3:
            continue
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string] += 1
        else:
            anagram_dict[sorted_string] = 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count <= 11