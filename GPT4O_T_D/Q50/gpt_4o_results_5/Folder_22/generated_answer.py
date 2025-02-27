from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            canonical = canonical_form(s)
            anagram_count[canonical] += 1
    total_pairs = 0
    for count in anagram_count.values():
        if count > 1:
            total_pairs += count * (count - 1) // 2
        if total_pairs >= 72:
            return True
    return False