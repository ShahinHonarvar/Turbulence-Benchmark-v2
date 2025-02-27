def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        key = ''.join(sorted(string.lower()))
        str_dict.setdefault(key, []).append(string)
    anagram_count = 0
    for anagram_list in str_dict.values():
        for i in range(len(anagram_list)):
            for j in range(i + 1, len(anagram_list)):
                if len(anagram_list[i]) >= 3 and len(anagram_list[j]) >= 3:
                    anagram_count += 1
    return anagram_count >= 155