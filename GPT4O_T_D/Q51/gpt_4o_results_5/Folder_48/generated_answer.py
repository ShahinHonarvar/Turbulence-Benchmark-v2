from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted((c for c in s.lower() if c.isalpha())))
    anagrams = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            key = sorted_chars(s)
            anagrams[key] += 1
    count = 0
    for value in anagrams.values():
        if value > 1:
            count += value * (value - 1) // 2
            if count > 277:
                return False
    return True