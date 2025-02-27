def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_dict[sorted_string] = anagram_dict.get(sorted_string, 0) + 1
    anagram_pairs = sum((value * (value - 1) // 2 for value in anagram_dict.values()))
    return anagram_pairs >= 209