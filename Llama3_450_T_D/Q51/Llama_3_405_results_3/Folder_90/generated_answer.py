def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(s)
            else:
                anagram_dict[sorted_str] = [s]
    anagram_count = 0
    for v in anagram_dict.values():
        anagram_count += len(v) * (len(v) - 1) // 2
        if anagram_count > 147:
            return False
    return True