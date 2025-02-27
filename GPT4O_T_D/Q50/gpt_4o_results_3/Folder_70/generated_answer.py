from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            form = canonical_form(string)
            anagram_count[form] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs >= 189