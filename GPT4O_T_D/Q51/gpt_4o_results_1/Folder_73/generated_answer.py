from collections import defaultdict

def if_contains_anagrams(strings):
    freq = defaultdict(int)
    for string in strings:
        sorted_chars = ''.join(sorted((c.lower() for c in string if c.isalpha())))
        if len(sorted_chars) >= 3:
            freq[sorted_chars] += 1
    pairs = sum((count * (count - 1) // 2 for count in freq.values() if count > 1))
    return pairs <= 279