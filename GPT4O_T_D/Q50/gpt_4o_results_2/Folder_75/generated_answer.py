from collections import defaultdict

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    sorted_strings = defaultdict(int)
    for s in strings:
        sorted_s = ''.join(sorted(s))
        sorted_strings[sorted_s] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in sorted_strings.values()))
    return anagram_pairs >= 70