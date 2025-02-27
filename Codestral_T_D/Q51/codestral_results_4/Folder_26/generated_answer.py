def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            if key not in anagram_dict:
                anagram_dict[key] = 0
            anagram_dict[key] += 1
    return sum((val * (val - 1) // 2 for val in anagram_dict.values())) <= 35