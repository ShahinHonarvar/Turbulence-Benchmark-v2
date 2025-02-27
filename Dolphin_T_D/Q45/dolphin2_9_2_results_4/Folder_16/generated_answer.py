from itertools import permutations

def palindromes_between_indices(s):
    letters = [ch for ch in s[6:10] if ch.isalpha()]
    palindromes = set()
    for p in permutations(''.join(letters), len(letters) // 2):
        for o in permutations(p):
            if ''.join(o) == ''.join(o[::-1]):
                palindromes.add(''.join(o))
    return palindromes if len(list(palindromes)) > 0 else set([''])