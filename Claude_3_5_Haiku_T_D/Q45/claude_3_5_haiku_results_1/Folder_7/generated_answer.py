from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:10] if char.isalpha()]
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for perm in permutations(letters, length):
            for p in range(len(perm)):
                candidate = list(perm)
                for q in range(len(candidate) // 2):
                    candidate[q], candidate[-(q + 1)] = (candidate[-(q + 1)], candidate[q])
                pal = ''.join(candidate)
                if pal == pal[::-1] and len(pal) >= 7:
                    palindromes.add(pal)
    return palindromes