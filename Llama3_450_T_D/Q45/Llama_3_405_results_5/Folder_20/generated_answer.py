def palindromes_between_indices(s):

    def is_palindrome(string):
        return string == string[::-1]
    letters = [c.lower() for c in s[2:9] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combo in set((''.join(p) for p in itertools.permutations(letters, length))):
            if is_palindrome(combo):
                palindromes.add(combo)
    return palindromes