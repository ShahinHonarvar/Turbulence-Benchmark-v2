from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s))
    anagram_count = defaultdict(int)
    strings = [s.lower() for s in strings if len(s) >= 3]
    for string in strings:
        sorted_s = sorted_str(string)
        anagram_count[sorted_s] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs <= 68