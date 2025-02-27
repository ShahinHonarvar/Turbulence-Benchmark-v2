from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter()
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            counter[sorted_string] += 1
    for value in counter.values():
        if value > 1:
            if value // 2 > 9:
                return False
    return True