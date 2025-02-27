from collections import Counter

def if_contains_anagrams(lst):
    word_counters = Counter((''.join(sorted(word.lower())) for word in lst if len(word) >= 3))
    pair_count = sum((count * (count - 1) // 2 for count in word_counters.values()))
    return pair_count >= 17