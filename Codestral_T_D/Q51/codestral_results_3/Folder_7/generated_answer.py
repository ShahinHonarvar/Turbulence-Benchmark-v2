from collections import Counter

def if_contains_anagrams(words):
    counter = Counter()
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            counter[sorted_word] += 1
    anagram_pairs = sum((n * (n - 1) // 2 for n in counter.values()))
    return anagram_pairs <= 445