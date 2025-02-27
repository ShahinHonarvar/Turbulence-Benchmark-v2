def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s] += 1
            else:
                anagram_dict[sorted_s] = 1
    count = 0
    for value in anagram_dict.values():
        count += value * (value - 1) // 2
    return count >= 21