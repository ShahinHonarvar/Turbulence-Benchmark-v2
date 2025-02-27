from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    str_dict = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        str_dict[sorted_s].append(s)
    for key in str_dict:
        if len(str_dict[key]) > 1:
            n = len(str_dict[key])
            anagram_count += n * (n - 1) // 2
    return anagram_count >= 155