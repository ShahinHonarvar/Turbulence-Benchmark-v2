import re
    from collections import defaultdict

def palindromes_between_indices(s):
    letters = defaultdict(int)
    for i in range(8):
        letters[s[i].lower()] += 1
    palindromes = set()
    for combo in itertools.product(string.ascii_lowercase, repeat=7):
        combo = ''.join(combo)
        if letters[combo[0].lower()] >= combo.count(combo[0]):
            if combo == combo[::-1]:
                palindromes.add(combo)
    return palindromes