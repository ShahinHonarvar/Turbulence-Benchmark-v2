def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:10] if c.isalpha()]

    def generate_palindromes(chars, current='', used=None):
        if used is None:
            used = set()
        if len(current) >= 5:
            if current == current[::-1]:
                palindromes.add(current)
        for i, char in enumerate(chars):
            if i not in used:
                generate_palindromes(chars, current + char, used | {i})
                generate_palindromes(chars, char + current, used | {i})
    palindromes = set()
    generate_palindromes(letters)
    return palindromes