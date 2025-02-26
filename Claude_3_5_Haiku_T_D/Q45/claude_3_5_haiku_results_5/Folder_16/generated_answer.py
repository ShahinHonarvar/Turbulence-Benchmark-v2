from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[6:10] if c.isalpha()))
    if len(letters) < 5:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters, len(letters))):
        chars = list(perm)
        if len(chars) >= 5:
            for i in range(len(chars) - 4):
                subset = chars[i:i + 5]
                if subset == subset[::-1]:
                    unique_palindromes.add(''.join(subset))
    return unique_palindromes