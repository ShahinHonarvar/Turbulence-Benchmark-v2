def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in anagram_dict:
                anagram_dict[sorted_s] = [s]
            else:
                anagram_dict[sorted_s].append(s)
    count = 0
    for anagrams in anagram_dict.values():
        if len(anagrams) >= 2:
            count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 39