def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string] += 1
            else:
                anagram_dict[sorted_string] = 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_dict.values()))
    return anagram_pairs >= 66