def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    for k in anagram_dict:
        count += anagram_dict[k] * (anagram_dict[k] - 1) // 2
    return count >= 153