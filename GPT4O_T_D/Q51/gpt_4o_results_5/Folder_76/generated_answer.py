from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagram_groups[sorted_chars(s)].append(s)
    for group in anagram_groups.values():
        if len(group) > 1:
            n = len(group)
            anagram_count += n * (n - 1) // 2
            if anagram_count > 91:
                return False
    return True