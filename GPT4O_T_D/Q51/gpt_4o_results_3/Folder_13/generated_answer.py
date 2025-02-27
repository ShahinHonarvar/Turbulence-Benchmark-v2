def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    pair_count = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return pair_count <= 54