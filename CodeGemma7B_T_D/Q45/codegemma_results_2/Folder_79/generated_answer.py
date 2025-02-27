from collections import defaultdict

def palindromes_between_indices(string):
    letters = defaultdict(set)
    for i, char in enumerate(string[1:8], start=1):
        letters[i - 1].add(char.lower())
    candidates = [''.join(sorted(chars)) for chars in letters.values()]
    return {word for word in candidates if word == word[::-1] and len(word) >= 3}