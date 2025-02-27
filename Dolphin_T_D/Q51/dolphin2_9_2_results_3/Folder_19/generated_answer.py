from collections import Counter

def if_contains_anagrams(lst):
    result = 0
    lst = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    counter = Counter(lst)
    pairs = sum([count * (count - 1) // 2 for count in counter.values() if count > 1])
    return pairs <= 69