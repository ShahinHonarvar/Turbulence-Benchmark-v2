from collections import defaultdict

def if_contains_anagrams(strings):

    def signature(s):
        return ''.join(sorted(s.lower()))
    counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            sig = signature(s)
            counts[sig] += 1
    num_pairs = 0
    for count in counts.values():
        if count > 1:
            num_pairs += count * (count - 1) // 2
            if num_pairs > 84:
                return False
    return True