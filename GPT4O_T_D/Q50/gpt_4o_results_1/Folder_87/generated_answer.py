from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            key = sorted_string(s)
            anagram_groups[key].append(s)
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            anagram_count += n * (n - 1) // 2
            if anagram_count >= 88:
                return True
    return False