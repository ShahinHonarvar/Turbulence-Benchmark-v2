def if_contains_anagrams(string_list):
    anagram_dict = {}
    anagram_count = 0
    for s in string_list:
        if len(s) >= 3 and s.isalpha():
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagram_dict:
                anagram_count += anagram_dict[sorted_str]
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    return anagram_count <= 15