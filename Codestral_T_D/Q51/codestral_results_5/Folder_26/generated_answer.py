def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for s in strings:
        lower_s = s.lower()
        if len(lower_s) < 3:
            continue
        sorted_s = ''.join(sorted(lower_s))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(lower_s)
        else:
            anagram_dict[sorted_s] = [lower_s]
    for anagrams in anagram_dict.values():
        anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
        if anagram_count > 35:
            return False
    return True