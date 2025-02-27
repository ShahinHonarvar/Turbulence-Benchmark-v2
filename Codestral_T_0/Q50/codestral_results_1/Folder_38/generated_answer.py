def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string] += 1
            else:
                anagram_dict[sorted_string] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs >= 24