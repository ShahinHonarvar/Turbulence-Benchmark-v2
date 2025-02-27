from collections import Counter

def if_contains_anagrams(words):
    counter = Counter()
    for word in words:
        lower_word = word.lower()
        if len(lower_word) >= 3:
            counter[tuple(sorted(lower_word))] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in counter.values()))
    return anagram_pairs <= 14