def palindromes_between_indices(s):
    letters = [c for c in s[3:8].lower() if c.isalpha()]
    palindromes = set()

    def find_palindromes(letters, current, remaining):
        if len(current) >= 3 and current == current[::-1]:
            palindromes.add(''.join(current))
        for i in range(len(letters)):
            find_palindromes(letters[:i] + letters[i + 1:], current + [letters[i]], remaining - 1)
    find_palindromes(letters, [], 6)
    return {p for p in palindromes if len(p) >= 6}