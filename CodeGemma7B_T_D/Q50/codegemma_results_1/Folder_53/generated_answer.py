from collections import defaultdict, Counter

def if_contains_anagrams(str_list):
    pairs = defaultdict(int)
    for string in str_list:
        if len(string) < 3:
            continue
        letters = Counter(string.lower())
        pairs[tuple(sorted(letters.values()))] += 1
    return any((count >= 11 for count in pairs.values()))