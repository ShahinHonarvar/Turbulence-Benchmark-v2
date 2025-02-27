def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(s)
            else:
                anagram_dict[sorted_str] = [s]
    count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            n = len(anagram_dict[key])
            count += n * (n - 1) // 2
    return count >= 24