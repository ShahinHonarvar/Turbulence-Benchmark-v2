def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for s in string_list:
        if len(s) < 3:
            continue
        s = ''.join(sorted(s.lower()))
        if s in anagram_dict:
            anagram_dict[s] += 1
        else:
            anagram_dict[s] = 1
    for k, v in anagram_dict.items():
        if v > 1:
            count += v * (v - 1) // 2
        if count >= 42:
            return True
    return False