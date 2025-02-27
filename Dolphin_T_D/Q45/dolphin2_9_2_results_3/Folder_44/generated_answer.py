from itertools import permutations

def palindromes_between_indices(s: str):
    letters = ''.join([c for c in s[2:8] if c.isalpha()])
    palindromes = set()
    for i in range(len(letters), 0, -1):
        for permut in permutations(letters, i):
            for p in ''.join(permut):
                if ''.join(permut).lower() == ''.join(permut)[::-1].lower():
                    palindromes.add(''.join(permut))
    return palindromes