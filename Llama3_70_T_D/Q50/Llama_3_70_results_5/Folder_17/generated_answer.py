def if_contains_anagrams(strings):
    anagram_dict = {}
    anagram_count = 0
    for string in strings:
        if len(string) < 3:
            continue
        string_lower = string.lower()
        string_sorted = ''.join(sorted(string_lower))
        if string_sorted in anagram_dict:
            anagram_dict[string_sorted] += 1
        else:
            anagram_dict[string_sorted] = 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 97