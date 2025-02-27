def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s] += 1
        else:
            anagram_dict[sorted_s] = 1
    anagram_pairs = sum([n * (n - 1) // 2 for n in anagram_dict.values()])
    return anagram_pairs >= 24