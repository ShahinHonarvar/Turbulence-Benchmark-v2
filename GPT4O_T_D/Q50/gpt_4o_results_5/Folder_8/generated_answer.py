def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    anagram_pairs = 0
    for count in anagram_dict.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 85