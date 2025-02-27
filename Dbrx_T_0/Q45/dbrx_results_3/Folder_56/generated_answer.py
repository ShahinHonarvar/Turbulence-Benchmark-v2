from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[5:10].lower()
    letters = set(substr) & english_letters
    if len(letters) < 2:
        return set()
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for combo in itertools.combinations(letters, length):
            combo = ''.join(combo)
            if combo == combo[::-1]:
                palindromes.add(combo)
    return palindromes