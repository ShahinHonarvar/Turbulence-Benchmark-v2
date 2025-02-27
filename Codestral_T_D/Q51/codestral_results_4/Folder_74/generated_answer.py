from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            counter = Counter(lower_string)
            key = tuple(sorted(counter.items()))
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    count = 0
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count <= 57