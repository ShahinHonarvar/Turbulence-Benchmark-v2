from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_counts[sorted_string] += 1
    for count in anagram_counts.values():
        if count >= 188:
            return True
    return False