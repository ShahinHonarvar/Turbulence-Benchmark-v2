from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        sorted_chars = ''.join(sorted(filter(str.isalpha, string.lower())))
        if len(sorted_chars) >= 3:
            anagrams[sorted_chars].append(string)
    count = 0
    for group in anagrams.values():
        n = len(group)
        count += n * (n - 1) // 2
        if count > 416:
            return False
    return True