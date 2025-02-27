from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2) and len(s1) >= 3
    lowercased_strings = [s.lower() for s in strings]
    anagram_groups = defaultdict(list)
    for s in lowercased_strings:
        normalized = ''.join(sorted(s))
        anagram_groups[normalized].append(s)
    count = 0
    for group in anagram_groups.values():
        n = len(group)
        if n >= 2:
            count += n * (n - 1) // 2
        if count > 276:
            return False
    return True