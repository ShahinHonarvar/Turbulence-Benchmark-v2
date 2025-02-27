from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    string_counts = [Counter(s) for s in strings]
    count = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if string_counts[i] == string_counts[j]:
                count += 1
    return count <= 423