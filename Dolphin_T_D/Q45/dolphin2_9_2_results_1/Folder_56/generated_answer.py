from itertools import permutations
    from string import ascii_letters

def palindromes_between_indices(s):
    substring = s[5:10].lower()
    pals = []
    for length in range(5, len(substring) + 1):
        for perm in permutations(substring, length):
            pal = ''.join(perm)
            if pal == pal[::-1]:
                pals.append(pal)
    return set(pals)