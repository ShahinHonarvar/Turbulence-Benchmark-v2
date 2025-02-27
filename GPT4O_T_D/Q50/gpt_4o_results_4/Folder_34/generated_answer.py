from collections import defaultdict

def if_contains_anagrams(string_list):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for string in string_list:
        if len(string) >= 3:
            sorted_str = sort_string(string)
            anagram_dict[sorted_str].append(string)
    count = 0
    for key in anagram_dict:
        n = len(anagram_dict[key])
        if n > 1:
            count += n * (n - 1) // 2
    return count >= 25