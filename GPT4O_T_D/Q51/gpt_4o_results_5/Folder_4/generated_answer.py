from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    seen = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            normalized = normalize(s)
            anagram_count += seen[normalized]
            if anagram_count > 84:
                return False
            seen[normalized] += 1
    return True