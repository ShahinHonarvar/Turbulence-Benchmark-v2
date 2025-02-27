def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        if len(string) >= 3:
            key = ''.join(sorted(string.lower()))
            if key not in anagram_dict:
                anagram_dict[key] = 0
            anagram_dict[key] += 1
    anagram_pairs = sum((value * (value - 1) // 2 for value in anagram_dict.values()))
    return anagram_pairs <= 52