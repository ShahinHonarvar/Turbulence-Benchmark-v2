from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_pairs[sorted_string].append(string)
    count = 0
    for group in anagram_pairs.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count <= 39