def palindromes_between_indices(s):
    letters = [c.lower() for c in s[6:10] if c.isalpha()]

    def generate_palindromes(chars, current='', palindromes=set()):
        if len(current) >= 4:
            palindromes.add(current)
        for i, char in enumerate(chars):
            generate_palindromes(chars[:i] + chars[i + 1:], char + current + char, palindromes)
        return palindromes
    return generate_palindromes(letters)