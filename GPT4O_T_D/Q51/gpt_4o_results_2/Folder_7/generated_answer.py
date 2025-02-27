from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    anagrams = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagrams[sorted_str] += 1
    for val in anagrams.values():
        if val > 1:
            count += val * (val - 1) // 2
            if count > 445:
                return False
    return count <= 445