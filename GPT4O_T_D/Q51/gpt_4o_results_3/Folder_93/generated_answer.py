from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s))
    count = 0
    seen = defaultdict(int)
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        form = canonical_form(s)
        seen[form] += 1
    for value in seen.values():
        count += value * (value - 1) // 2
        if count > 36:
            return False
    return True