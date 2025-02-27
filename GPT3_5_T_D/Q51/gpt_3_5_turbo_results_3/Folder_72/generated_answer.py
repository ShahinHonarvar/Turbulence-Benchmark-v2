from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    counts = [Counter(s) for s in strings]
    anagram_pairs = 0
    for i in range(len(counts)):
        for j in range(i + 1, len(counts)):
            if counts[i] == counts[j]:
                anagram_pairs += 1
    return anagram_pairs <= 188