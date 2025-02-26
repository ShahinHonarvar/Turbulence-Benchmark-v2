def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:8] if c.isalpha()]

    def generate_palindromes(chars, current='', min_length=7):
        if len(current) >= min_length and current == current[::-1]:
            palindromes.add(current)
        for i, char in enumerate(chars):
            generate_palindromes(chars[:i] + chars[i + 1:], char + current + char, min_length)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes