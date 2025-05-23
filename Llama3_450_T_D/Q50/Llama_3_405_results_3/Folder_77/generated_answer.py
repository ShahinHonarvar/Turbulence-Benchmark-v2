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
    for key in anagram_dict:
        count += anagram_dict[key] * (anagram_dict[key] - 1) // 2
    return count >= 209