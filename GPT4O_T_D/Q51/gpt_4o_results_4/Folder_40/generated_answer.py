from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    counters = defaultdict(int)
    for word in strings:
        if len(word) >= 3:
            counters[sorted_string(word)] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in counters.values()))
    return anagram_pairs <= 29