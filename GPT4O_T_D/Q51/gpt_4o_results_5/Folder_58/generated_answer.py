from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    strings = [s for s in strings if len(s) >= 3]
    counter = Counter((normalize(s) for s in strings))
    pairs = sum((count * (count - 1) // 2 for count in counter.values()))
    return pairs <= 60