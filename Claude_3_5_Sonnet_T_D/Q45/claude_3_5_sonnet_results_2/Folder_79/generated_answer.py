def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[1:8] if c.isalpha()))
    palindromes = set()

    def generate_palindromes(chars, current=''):
        if len(current) >= 3 and current == current[::-1]:
            palindromes.add(current)
        for i, char in enumerate(chars):
            generate_palindromes(chars[:i] + chars[i + 1:], current + char)
    generate_palindromes(letters)
    return palindromes