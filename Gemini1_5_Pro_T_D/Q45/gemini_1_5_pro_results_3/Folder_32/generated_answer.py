from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    string = string[1:8].lower()
    letters = [letter for letter in string if letter.isalpha()]
    counts = Counter(letters)
    center = ''
    half = ''
    for letter, count in counts.items():
        if count % 2 == 1:
            if center:
                return set()
            center = letter * count
        half += letter * (count // 2)
    if len(center) + len(half) * 2 < 5:
        return set()
    perms = set([''.join(p) for p in permutations(half)])
    if not center:
        return {p + p[::-1] for p in perms}
    return {p + center + p[::-1] for p in perms}