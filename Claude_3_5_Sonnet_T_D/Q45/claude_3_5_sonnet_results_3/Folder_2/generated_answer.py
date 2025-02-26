def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:6] if c.isalpha()]

    def generate_palindromes(chars, current='', length=0):
        if length >= 6:
            if current == current[::-1]:
                palindromes.add(current)
        for i, char in enumerate(chars):
            generate_palindromes(chars[:i] + chars[i + 1:], char + current + char, length + 2)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes