from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_str = sort_string(string)
            anagram_dict[sorted_str].append(string)
    count = 0
    for anagram_group in anagram_dict.values():
        n = len(anagram_group)
        count += n * (n - 1) // 2
        if count > 29:
            return False
    return True