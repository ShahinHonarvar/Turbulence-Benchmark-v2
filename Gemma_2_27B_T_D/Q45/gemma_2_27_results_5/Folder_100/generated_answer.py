from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:6])).lower()
    return set((p[0:len(p) // 2] + (p[flip] if len(p) % 2 else '') + ''.join(reversed(p[0:len(p) // 2])) for p in permutations(letters) if len(p) >= 6 and p[0:len(p) // 2] == ''.join(reversed(p[0:len(p) // 2]))))