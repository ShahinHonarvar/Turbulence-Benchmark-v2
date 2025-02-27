from collections import defaultdict

def if_contains_anagrams(strings):
    counter = defaultdict(int)
    for string in strings:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            counter[sorted_string] += 1
    return sum((n * (n - 1) for n in counter.values())) <= 464