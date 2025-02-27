from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_groups = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            key = sorted_string(string)
            anagram_count += anagram_groups[key]
            anagram_groups[key] += 1
    return anagram_count >= 246