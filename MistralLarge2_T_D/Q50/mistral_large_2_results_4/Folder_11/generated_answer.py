from collections import defaultdict

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagram_count = defaultdict(int)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        anagram_count[sorted_string] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return anagram_pairs >= 28