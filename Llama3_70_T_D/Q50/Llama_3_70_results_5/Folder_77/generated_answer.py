def if_contains_anagrams(lst):
    anagram_dict = {}
    count = 0
    for string in lst:
        sorted_str = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    for value in anagram_dict.values():
        count += value * (value - 1) // 2
    return count >= 209