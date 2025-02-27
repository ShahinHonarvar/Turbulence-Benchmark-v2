from collections import Counter

def if_contains_anagrams(list_of_strings):
    counter = Counter()
    for word in list_of_strings:
        if len(word) >= 3:
            counter[word.lower()] += 1
    pairs_of_anagrams = sum((n * (n - 1) // 2 for n in counter.values() if n > 1))
    return pairs_of_anagrams >= 26