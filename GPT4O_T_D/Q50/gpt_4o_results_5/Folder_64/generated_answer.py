def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    anagram_pairs = sum((v // 2 for v in anagram_dict.values()))
    return anagram_pairs >= 5