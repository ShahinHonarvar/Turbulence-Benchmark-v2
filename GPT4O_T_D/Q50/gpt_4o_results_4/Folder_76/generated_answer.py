from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    count = 0
    anagrams = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = sorted_string(string)
            anagrams[sorted_str] += 1
    for val in anagrams.values():
        if val > 1:
            count += val * (val - 1) // 2
    return count >= 143