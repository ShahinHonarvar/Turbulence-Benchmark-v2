from collections import defaultdict

def if_contains_anagrams(strings):
    count = defaultdict(int)
    for string in strings:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            count[sorted_string] += 1
    num_anagrams = sum((v * (v - 1) // 2 for v in count.values() if v > 1))
    return num_anagrams <= 60