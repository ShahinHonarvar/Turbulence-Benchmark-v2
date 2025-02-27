from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    anagrams = defaultdict(list)
    for string in strings:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            anagrams[sorted_str].append(string)
    for group in anagrams.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
            if count >= 78:
                return True
    return False