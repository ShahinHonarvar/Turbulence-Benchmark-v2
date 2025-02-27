def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3 and sorted_str.isalpha():
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(s)
            else:
                anagram_dict[sorted_str] = [s]
    anagram_count = 0
    for k in anagram_dict:
        anagram_count += len(anagram_dict[k]) * (len(anagram_dict[k]) - 1) // 2
    return anagram_count <= 85