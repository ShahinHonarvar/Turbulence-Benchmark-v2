from collections import Counter

def if_contains_anagrams(strings):
    c = Counter()
    for string in strings:
        if len(string) >= 3:
            c[tuple(sorted(string.lower()))] += 1
    return len([value for value in c.values() if value >= 2]) >= 54