from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_lower(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            key = sorted_lower(s)
            anagram_groups[key].append(s)
    count = 0
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            count += n * (n - 1) // 2
            if count >= 46:
                return True
    return False