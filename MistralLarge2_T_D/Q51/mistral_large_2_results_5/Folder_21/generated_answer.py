from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_count[sorted_string].append(string)
    pair_count = sum((len(group) * (len(group) - 1) // 2 for group in anagram_count.values() if len(group) > 1))
    return pair_count <= 26