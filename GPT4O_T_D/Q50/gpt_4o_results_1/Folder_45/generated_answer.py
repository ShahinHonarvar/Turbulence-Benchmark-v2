from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            anagram_groups[sorted_chars(string)].append(string)
    anagram_count = 0
    for group in anagram_groups.values():
        if len(group) > 1:
            n = len(group)
            anagram_count += n * (n - 1) // 2
            if anagram_count >= 277:
                return True
    return False