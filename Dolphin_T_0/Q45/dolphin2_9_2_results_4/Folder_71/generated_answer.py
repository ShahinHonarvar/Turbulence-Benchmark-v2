def palindromes_between_indices(s):
    chars = [c.lower() for c in s[1:4]]
    letters = set(''.join(filter(str.isalpha, chars)))
    if len(letters) < 2:
        return set()
    return {''.join(p) for i in range(len(letters)) for j in range(i, len(letters)) if letters.pop() != letters.pop() != letters.pop() != letters.pop() for p in permutations(letters.pop(i), letters.pop(j))}