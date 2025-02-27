def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for string in strings:
        normalized_string = ''.join(sorted(string.lower()))
        if len(normalized_string) < 3:
            continue
        if normalized_string in anagram_dict:
            anagram_dict[normalized_string] += 1
        else:
            anagram_dict[normalized_string] = 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count <= 91