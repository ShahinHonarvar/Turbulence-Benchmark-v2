from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    lower_counts = defaultdict(int)
    for word in list_of_strings:
        lower_counts[''.join(sorted([c for c in word.lower() if c.isalpha()]))] += 1
    pairs = 0
    for count in lower_counts.values():
        pairs += count * (count - 1) // 2
    if pairs >= 219:
        return True
    return False