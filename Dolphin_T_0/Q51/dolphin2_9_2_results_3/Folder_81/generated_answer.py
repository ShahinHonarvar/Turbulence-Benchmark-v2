from collections import Counter

def if_contains_anagrams(lst):

    def process(word):
        return ''.join(sorted(word.lower()))
    count = Counter()
    pairs = 0
    for word in lst:
        if len(word) >= 3:
            sorted_word = process(word)
            count[sorted_word] += 1
    for value in count.values():
        pairs += value * (value - 1) // 2
    return pairs <= 79