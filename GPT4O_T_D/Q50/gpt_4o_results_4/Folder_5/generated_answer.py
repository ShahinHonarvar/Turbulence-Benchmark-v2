from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s))
    anagrams = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = sort_string(string.lower())
            anagrams[sorted_str] += 1
    count = 0
    for value in anagrams.values():
        if value > 1:
            count += value * (value - 1) // 2
    return count >= 21