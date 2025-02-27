def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for s in strings:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3 and s.isalpha():
            if s in anagram_dict:
                anagram_dict[s] += 1
            else:
                anagram_dict[s] = 1
    for v in anagram_dict.values():
        count += v * (v - 1) // 2
    return count <= 475