def if_contains_anagrams(string_list):
    cleaned_list = [''.join(filter(str.isalpha, s.lower())) for s in string_list]
    anagram_dict = {}
    for s in cleaned_list:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_dict[sorted_s] = anagram_dict.get(sorted_s, 0) + 1
    anagram_pairs = sum((count // 2 for count in anagram_dict.values()))
    return anagram_pairs <= 3