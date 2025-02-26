def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:7] if c.isalpha()]

    def generate_palindromes(chars, current='', length=0):
        if length >= 4:
            if current == current[::-1]:
                palindromes.add(current)
        for i, char in enumerate(chars):
            generate_palindromes(chars[:i] + chars[i + 1:], current + char, length + 1)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes