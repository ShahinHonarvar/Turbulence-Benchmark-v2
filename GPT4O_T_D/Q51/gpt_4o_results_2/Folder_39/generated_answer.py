from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(set)
    for string in strings:
        normalized = ''.join(filter(str.isalpha, string))
        if len(normalized) >= 3:
            sorted_norm = sorted_string(normalized)
            anagram_dict[sorted_norm].add(string.lower())
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_dict.values()))
    return anagram_pairs <= 257