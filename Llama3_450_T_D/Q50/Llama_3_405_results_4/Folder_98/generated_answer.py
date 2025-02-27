def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagram_dict:
            anagram_dict[sorted_str].append(s)
        else:
            anagram_dict[sorted_str] = [s]
    anagram_pairs = 0
    for value in anagram_dict.values():
        if len(value) > 1:
            anagram_pairs += len(value) * (len(value) - 1) // 2
    return anagram_pairs >= 7