from collections import defaultdict

def if_contains_anagrams(str_list):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(list)
    for string in str_list:
        sorted_str1 = sorted_str(string)
        if len(sorted_str1) >= 3:
            anagrams[sorted_str1].append(string)
    return len(anagrams) <= 91