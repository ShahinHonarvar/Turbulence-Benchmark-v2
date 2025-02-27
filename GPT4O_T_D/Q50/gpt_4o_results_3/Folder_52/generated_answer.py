from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    sorted_strings = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            sorted_strings[sorted_s] += 1
    for count in sorted_strings.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count >= 58