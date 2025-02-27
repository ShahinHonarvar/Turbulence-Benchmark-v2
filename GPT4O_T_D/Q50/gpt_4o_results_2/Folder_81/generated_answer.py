from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagrams[sorted_str].append(string)
    for group in anagrams.values():
        n = len(group)
        count += n * (n - 1) // 2
        if count >= 16:
            return True
    return False