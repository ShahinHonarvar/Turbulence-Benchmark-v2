from collections import defaultdict

def if_contains_anagrams(strings):
    count = defaultdict(int)
    for string in strings:
        string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            count[string] += 1
    return any((v > 1 for v in count.values()))