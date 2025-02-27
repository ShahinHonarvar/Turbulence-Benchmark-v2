from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    str_dict = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        str_dict[sorted_str].append(string)
    for key in str_dict:
        if len(str_dict[key]) > 1:
            anagram_count += len(str_dict[key]) * (len(str_dict[key]) - 1) // 2
    return anagram_count >= 46