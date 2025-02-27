def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(s)
        else:
            anagram_dict[sorted_s] = [s]
    anagram_count = sum((len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in anagram_dict.values()))
    return anagram_count >= 209