from collections import Counter

def if_contains_anagrams(list_of_strings):
    counter = Counter()
    for string in list_of_strings:
        if len(string) >= 3:
            counter[tuple(sorted(string.lower()))] += 1
    for count in counter.values():
        if count >= 29:
            return True
    return False