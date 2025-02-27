def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) < 3:
            continue
        if sorted_str in anagram_dict:
            anagram_dict[sorted_str].append(s)
        else:
            anagram_dict[sorted_str] = [s]
    count = 0
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 96