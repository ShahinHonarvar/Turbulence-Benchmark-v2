def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = {}
    for s in string_list:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            if key not in anagram_dict:
                anagram_dict[key] = 1
            else:
                anagram_dict[key] += 1
                anagram_count += anagram_dict[key] - 1
    return anagram_count <= 42