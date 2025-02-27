from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = sort_string(string)
            anagram_dict[sorted_str] += 1
    anagram_pairs = 0
    for count in anagram_dict.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 19