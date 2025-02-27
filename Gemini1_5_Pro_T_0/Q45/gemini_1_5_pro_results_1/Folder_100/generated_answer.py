from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = [string[i].lower() for i in range(6) if string[i].isalpha()]
    counts = Counter(letters)
    mid = ''
    half = ''
    for letter, count in counts.items():
        if count % 2 == 1:
            if mid:
                return set()
            mid = letter * count
        else:
            half += letter * (count // 2)
    if len(mid) > 1:
        return set()
    if len(half) < 3:
        return set()
    perms = set([''.join(p) for p in permutations(half)])
    palindromes = set()
    for perm in perms:
        palindromes.add(perm + mid + perm[::-1])
    return palindromes