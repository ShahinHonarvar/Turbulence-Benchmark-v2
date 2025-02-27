from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(set)
    for s in strings:
        if len(s) >= 3:
            norm = normalize(s)
            anagrams[norm].add(s.lower())
    count = 0
    for group in anagrams.values():
        n = len(group)
        if n > 1:
            count += n * (n - 1) // 2
            if count > 92:
                return False
    return True