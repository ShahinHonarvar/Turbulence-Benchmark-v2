from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = sorted_chars(string)
            anagram_dict[sorted_string].append(string)
    anagram_count = 0
    for anagram_list in anagram_dict.values():
        n = len(anagram_list)
        if n > 1:
            anagram_count += n * (n - 1) // 2
    return anagram_count <= 52