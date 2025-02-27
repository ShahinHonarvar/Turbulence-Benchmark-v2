from collections import Counter
import string

def if_contains_anagrams(list_of_strings):
    counter = Counter()
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in counter:
                counter[sorted_string] += 1
            else:
                counter[sorted_string] = 1
    pairs = sum([v * (v - 1) // 2 for v in counter.values()])
    return pairs <= 94