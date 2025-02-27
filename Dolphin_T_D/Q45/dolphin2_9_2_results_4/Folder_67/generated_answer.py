import itertools

def palindromes_between_indices(s):
    english_letters = [char for char in 'abcdefghijklmnopqrstuvwxyz']
    indices = [i for i in range(2, 7)]
    substring = ''.join([s[i] for i in indices])
    substring_letters = [char for char in substring if char.lower() in english_letters]
    length = len(substring_letters)
    palindromes = set()
    for i in range(length, 0, -1):
        for combo in itertools.combinations(substring_letters, i):
            for p in [''.join(p) for p in itertools.permutations(combo) if p == p[::-1]]:
                if len(p) >= 5:
                    palindromes.add(p)
    return palindromes