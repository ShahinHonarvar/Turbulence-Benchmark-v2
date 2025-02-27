from collections import Counter

def if_contains_anagrams(list_of_strings):
    counter = Counter([''.join(sorted(s.lower())) for s in list_of_strings if len(s) >= 3])
    return sum((n * (n - 1) // 2 for n in counter.values())) <= 48