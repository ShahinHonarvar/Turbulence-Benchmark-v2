from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_str = sorted_string(string)
            anagram_groups[sorted_str].append(string)
    anagram_pairs = 0
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
            if anagram_pairs > 54:
                return False
    return True