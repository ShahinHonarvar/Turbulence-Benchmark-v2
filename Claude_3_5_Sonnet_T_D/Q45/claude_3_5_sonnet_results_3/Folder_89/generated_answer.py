def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:10] if c.isalpha()]

    def generate_palindromes(chars, current=''):
        if len(current) >= 6 and current == current[::-1]:
            palindromes.add(current)
        for i, char in enumerate(chars):
            generate_palindromes(chars[:i] + chars[i + 1:], current + char)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes