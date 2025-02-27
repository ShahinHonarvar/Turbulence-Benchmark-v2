from collections import Counter

def if_contains_anagrams(arr):
    count = Counter()
    for word in arr:
        c = Counter(word.lower())
        if len(c) >= 3 and c not in count:
            count[c] = 1
        elif c in count:
            count[c] += 1
    anagram_pairs = sum(count.values())
    return anagram_pairs <= 34