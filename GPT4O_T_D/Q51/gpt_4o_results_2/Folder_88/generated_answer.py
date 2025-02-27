from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))

    def is_eligible(s):
        return len(s) >= 3
    eligible_strings = [s for s in strings if is_eligible(s)]
    anagram_map = defaultdict(int)
    for s in eligible_strings:
        key = canonical_form(s)
        anagram_map[key] += 1
    anagram_pairs = 0
    for count in anagram_map.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 407