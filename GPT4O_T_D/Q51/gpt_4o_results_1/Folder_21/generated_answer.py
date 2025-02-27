from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_lower(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            key = sorted_lower(string)
            anagram_groups[key].append(string)
    count = sum((len(values) * (len(values) - 1) // 2 for values in anagram_groups.values() if len(values) > 1))
    return count <= 26