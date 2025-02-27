def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        sorted_str = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            anagram_dict[sorted_str] = anagram_dict.get(sorted_str, 0) + 1
    count = sum((value * (value - 1) // 2 for value in anagram_dict.values() if value > 1))
    return count >= 84