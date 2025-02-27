def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        if key in anagram_dict:
            anagram_dict[key] += 1
        else:
            anagram_dict[key] = 1
    anagram_pairs = sum((val * (val - 1) // 2 for val in anagram_dict.values()))
    return anagram_pairs <= 61