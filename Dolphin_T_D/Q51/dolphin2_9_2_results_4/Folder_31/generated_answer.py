from collections import Counter

def if_contains_anagrams(list_of_strings):
    counter = Counter()
    for string in list_of_strings:
        if len(string) >= 3:
            counter[tuple(sorted(string.lower()))] += 1
    count = 0
    for key in counter.keys():
        if counter[key] > 1:
            count += counter[key]
    return True if count <= 65 else False