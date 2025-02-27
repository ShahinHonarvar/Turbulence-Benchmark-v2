from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_sets = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        anagram_sets[sorted_str].append(string)
    for group in anagram_sets.values():
        n = len(group)
        anagram_count += n * (n - 1) // 2
        if anagram_count >= 153:
            return True
    return False