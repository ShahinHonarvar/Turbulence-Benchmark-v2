def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    anagram_count = sum((count * (count - 1) // 2 for count in anagram_dict.values() if count > 1))
    return anagram_count >= 34