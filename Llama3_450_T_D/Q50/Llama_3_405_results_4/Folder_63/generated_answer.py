def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        if len(s) >= 3:
            sorted_string = ''.join(sorted(s.lower()))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(s)
            else:
                anagram_dict[sorted_string] = [s]
    anagram_count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            anagram_count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return anagram_count >= 89