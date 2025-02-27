from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    lower_strings = [s.lower() for s in strings if len(s) >= 3]
    anagram_groups = defaultdict(list)
    for s in lower_strings:
        key = ''.join(sorted(s))
        anagram_groups[key].append(s)
    count = 0
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            count += n * (n - 1) // 2
        if count >= 11:
            return True
    return False