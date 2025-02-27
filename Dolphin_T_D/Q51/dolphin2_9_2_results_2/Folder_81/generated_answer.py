from collections import Counter

def if_contains_anagrams(string_list):
    counter = Counter()
    for string in string_list:
        if len(string) >= 3:
            counter[tuple(sorted(string.lower()))] += 1
    return sum((i * (i - 1) // 2 <= 79 for i in counter.values())) == 1