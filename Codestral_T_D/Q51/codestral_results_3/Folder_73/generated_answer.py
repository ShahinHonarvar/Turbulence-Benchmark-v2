def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        if sorted_s not in anagram_dict:
            anagram_dict[sorted_s] = []
        anagram_dict[sorted_s].append(s)
    anagram_pairs = 0
    for anagrams in anagram_dict.values():
        anagram_pairs += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_pairs <= 279