from collections import Counter

def if_contains_anagrams(strings):
    lowercase_strings = [s.lower() for s in strings]
    anagrams = Counter()
    for s in lowercase_strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagrams.values() if count > 1))
    return anagram_pairs <= 94