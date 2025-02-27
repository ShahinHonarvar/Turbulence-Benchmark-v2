def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if sorted_s not in anagram_dict:
                anagram_dict[sorted_s] = 1
            else:
                anagram_dict[sorted_s] += 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 81