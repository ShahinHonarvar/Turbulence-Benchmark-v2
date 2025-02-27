from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            key = canonical_form(s)
            anagram_count[key] += 1
    total_pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return total_pairs <= 48