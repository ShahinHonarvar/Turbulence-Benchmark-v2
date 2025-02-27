def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for s in strings:
        lower_s = s.lower()
        if len(lower_s) >= 3:
            sorted_s = ''.join(sorted(lower_s))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s] += 1
            else:
                anagram_dict[sorted_s] = 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 78