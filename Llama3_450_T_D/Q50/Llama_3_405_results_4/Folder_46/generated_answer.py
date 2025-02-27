def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(s)
            else:
                anagram_dict[sorted_str] = [s]
    count = 0
    for v in anagram_dict.values():
        if len(v) > 1:
            count += len(v) * (len(v) - 1) // 2
    return count >= 38