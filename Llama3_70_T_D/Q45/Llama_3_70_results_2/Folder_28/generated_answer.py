def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:6] if c.isalpha()]
    palindromes = set()

    def generate_palindromes(letters, current, remaining):
        if len(current) == 2:
            palindromes.add(''.join(current + remaining + current[::-1]))
        for i in range(len(letters)):
            generate_palindromes(letters[:i] + letters[i + 1:], current + [letters[i]], remaining)
    for i in range(len(letters)):
        generate_palindromes(letters[:i] + letters[i + 1:], [letters[i]], letters[:i] + letters[i + 1:])
    return set((p for p in palindromes if len(p) >= 4))