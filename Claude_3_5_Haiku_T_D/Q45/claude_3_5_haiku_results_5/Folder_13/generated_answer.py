import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:10] if c.isalpha()]
    palindromes = set()

    def generate_palindromes(curr_letters):
        if len(curr_letters) >= 5:
            for perm in set((''.join(p) for p in itertools.permutations(curr_letters))):
                if perm == perm[::-1]:
                    palindromes.add(perm)
        for i in range(len(curr_letters)):
            generate_palindromes(curr_letters[:i] + curr_letters[i + 1:])
    generate_palindromes(letters)
    return palindromes