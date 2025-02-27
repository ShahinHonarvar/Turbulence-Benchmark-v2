from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in permutations(letters, r):
            if len(p) % 2 == 0:
                first_half = ''.join(p[:len(p) // 2])
                second_half = ''.join(p[len(p) // 2:])
                if first_half == second_half[::-1]:
                    palindromes.add(''.join(p))
            else:
                first_half = ''.join(p[:len(p) // 2])
                second_half = ''.join(p[len(p) // 2 + 1:])
                if first_half == second_half[::-1]:
                    palindromes.add(''.join(p))
    return palindromes