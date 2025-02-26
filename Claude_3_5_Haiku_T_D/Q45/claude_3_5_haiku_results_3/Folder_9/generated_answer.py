def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:7] if c.isalpha()]
    palindromes = set()

    def generate_palindromes(curr_letters):
        if len(curr_letters) >= 7:
            for perm in set((''.join(p) for p in __import__('itertools').permutations(curr_letters))):
                if perm == perm[::-1]:
                    palindromes.add(perm)
    for r in range(7, len(curr_letters) + 1):
        generate_palindromes(letters + [letters[i % len(letters)] for i in range(r - len(letters))])
    return palindromes