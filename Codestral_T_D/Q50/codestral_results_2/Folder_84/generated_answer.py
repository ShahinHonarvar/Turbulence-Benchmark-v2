from collections import defaultdict

def if_contains_anagrams(strings):
    count = defaultdict(int)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            count[sorted_string] += 1
    return sum((v * (v - 1) // 2 for v in count.values())) >= 108