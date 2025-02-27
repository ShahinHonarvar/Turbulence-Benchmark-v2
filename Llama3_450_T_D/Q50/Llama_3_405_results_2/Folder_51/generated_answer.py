def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(s)
            else:
                anagram_dict[sorted_str] = [s]
    count = 0
    for v in anagram_dict.values():
        if len(v) > 1:
            count += len(v) * (len(v) - 1) // 2
    return count >= 39