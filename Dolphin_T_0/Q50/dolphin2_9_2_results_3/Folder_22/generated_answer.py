from collections import Counter

def if_contains_anagrams(words):
    counter = Counter()
    for word in words:
        if len(word) >= 3:
            counter[tuple(sorted(word.lower()))] += 1
    count = sum((value * (value - 1) // 2 for value in counter.values() if value > 1))
    return count >= 72