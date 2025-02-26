from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    letter_count = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_chars = ''.join(sorted(s.lower()))
            letter_count[sorted_chars].append(s)
    for group in letter_count.values():
        n = len(group)
        if n > 1:
            anagram_count += n * (n - 1) // 2
    return anagram_count >= 246