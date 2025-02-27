from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical_form(word):
        return ''.join(sorted(word.lower()))
    anagram_map = defaultdict(int)
    count = 0
    for s in strings:
        if len(s) >= 3:
            form = canonical_form(s)
            anagram_map[form] += 1
    for value in anagram_map.values():
        if value > 1:
            count += value * (value - 1) // 2
            if count >= 16:
                return True
    return False