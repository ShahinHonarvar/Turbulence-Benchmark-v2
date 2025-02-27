from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_lower(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            key = sorted_lower(string)
            anagram_counts[key] += 1
    pairs = 0
    for count in anagram_counts.values():
        if count > 1:
            pairs += count * (count - 1) // 2
            if pairs >= 55:
                return True
    return False