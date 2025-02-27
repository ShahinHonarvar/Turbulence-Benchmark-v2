def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagram_dict:
            anagram_dict[sorted_str].append(s)
        else:
            anagram_dict[sorted_str] = [s]
    count = 0
    for k in anagram_dict:
        count += len(anagram_dict[k]) * (len(anagram_dict[k]) - 1) // 2
        if count > 16:
            return False
    return True