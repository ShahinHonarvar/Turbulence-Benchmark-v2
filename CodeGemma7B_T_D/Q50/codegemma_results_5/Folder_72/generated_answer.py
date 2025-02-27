from collections import Counter

def if_contains_anagrams(lst):
    str_counts = Counter((word.lower() for word in lst if len(word) >= 3))
    count = 0
    for word, freq in str_counts.items():
        for target in str_counts:
            if word != target and sorted(word) == sorted(target):
                count += freq * str_counts[target]
    return count >= 55