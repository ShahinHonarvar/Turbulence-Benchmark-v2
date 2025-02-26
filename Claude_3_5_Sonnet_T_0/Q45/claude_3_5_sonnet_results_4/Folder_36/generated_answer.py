def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:9] if c.isalpha()]

    def generate_palindromes(chars, current='', palindromes=set()):
        if len(current) >= 3 and current == current[::-1]:
            palindromes.add(current)
        for i, char in enumerate(chars):
            generate_palindromes(chars[:i] + chars[i + 1:], current + char, palindromes)
        return palindromes
    return generate_palindromes(letters)