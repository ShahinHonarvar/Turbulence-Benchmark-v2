def if_contains_anagrams(strs):
    anagram_dict = {}
    for s in strs:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(s)
        else:
            anagram_dict[sorted_s] = [s]
    count = 0
    for value in anagram_dict.values():
        count += len(value) * (len(value) - 1) // 2
    return count >= 41