from collections import defaultdict

def if_contains_anagrams(lst):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    count = 0
    anagram_dict = defaultdict(list)
    for string in lst:
        if len(string) >= 3:
            sorted_str = sort_string(string)
            anagram_dict[sorted_str].append(string)
    for key in anagram_dict:
        n = len(anagram_dict[key])
        if n > 1:
            count += n * (n - 1) // 2
        if count > 423:
            return False
    return True