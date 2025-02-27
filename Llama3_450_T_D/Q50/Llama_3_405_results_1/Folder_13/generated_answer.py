def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    count = 0
    for value in anagram_dict.values():
        count += value * (value - 1) // 2
    return count >= 144