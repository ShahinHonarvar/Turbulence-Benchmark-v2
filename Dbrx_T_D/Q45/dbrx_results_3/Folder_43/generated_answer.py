from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters_in_range = {ch.lower() for ch in s[2:6] if ch.lower() in english_letters}
    if len(letters_in_range) < 2:
        return set()
    palindromes = set()
    for length in range(4, len(letters_in_range) + 1):
        for combo in itertools.combinations(letters_in_range, length):
            combo = ''.join(combo)
            if combo + combo[-2::-1] in palindromes:
                continue
            palindromes.add(combo)
            palindromes.add(combo + combo[-2::-1])
    return palindromes