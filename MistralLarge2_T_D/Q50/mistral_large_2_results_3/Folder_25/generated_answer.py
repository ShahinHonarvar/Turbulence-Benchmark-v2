from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical(s):
        return ''.join(sorted(s.lower()))
    count = defaultdict(int)
    pairs = 0
    for string in strings:
        if len(string) < 3:
            continue
        canon = canonical(string)
        if count[canon] > 0:
            pairs += count[canon]
            count[canon] += 1
        else:
            count[canon] = 1
    return pairs >= 14