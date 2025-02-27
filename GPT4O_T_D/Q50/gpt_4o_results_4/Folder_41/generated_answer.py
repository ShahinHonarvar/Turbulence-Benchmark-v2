from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_string = sorted_str(string)
            anagram_dict[sorted_string] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values() if count > 1))
    return anagram_pairs >= 75