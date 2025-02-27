from collections import Counter

def if_contains_anagrams(strings):
    counter_of_anagrams = Counter()
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            counter_of_anagrams[sorted_s] += 1
    return any((count >= 2 for count in counter_of_anagrams.values()))