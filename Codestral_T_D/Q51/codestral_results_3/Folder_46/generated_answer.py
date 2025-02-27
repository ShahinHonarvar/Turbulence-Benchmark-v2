from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    anagram_counter = Counter()
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            count += anagram_counter[key]
            anagram_counter[key] += 1
    return count <= 61