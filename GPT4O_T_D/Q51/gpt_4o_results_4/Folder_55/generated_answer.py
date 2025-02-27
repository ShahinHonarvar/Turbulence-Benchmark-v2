from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagrams[sorted_str].append(string)
    for value in anagrams.values():
        n = len(value)
        if n > 1:
            count += n * (n - 1) // 2
    return count <= 44