from collections import defaultdict

def if_contains_anagrams(strings):
    counter = 0
    anagram_groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_groups[sorted_s].append(s)
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            counter += n * (n - 1) // 2
            if counter > 474:
                return False
    return True