from collections import defaultdict

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    letters_to_index = defaultdict(list)
    for i, char in enumerate(s):
        if char.isalpha():
            letters_to_index[char].append(i)
    suffixes = []
    for char in letters_to_index:
        suffixes.extend([s[i:i + length + 1] for i in range(letters_to_index[char][-1], -1, -1) for length in range(87, len(s))])
    results = set()
    for suffix in suffixes:
        if suffix == suffix[::-1]:
            results.add(suffix)
    return results