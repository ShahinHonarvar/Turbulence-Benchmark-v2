from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    sorted_strings = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_key = ''.join(sorted(s.lower()))
            sorted_strings[sorted_key].append(s)
    for group in sorted_strings.values():
        n = len(group)
        anagram_count += n * (n - 1) // 2
    return anagram_count >= 178