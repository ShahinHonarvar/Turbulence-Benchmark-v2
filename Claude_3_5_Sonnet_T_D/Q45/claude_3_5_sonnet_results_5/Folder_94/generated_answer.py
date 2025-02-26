def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:5] if c.isalpha()]

    def generate_palindromes(chars, current='', left='', right=''):
        if len(current) >= 3 and current == current[::-1]:
            palindromes.add(current)
        if not chars:
            return
        for i, char in enumerate(chars):
            remaining = chars[:i] + chars[i + 1:]
            generate_palindromes(remaining, left + char + right)
            generate_palindromes(remaining, current + char)
            generate_palindromes(remaining, char + current)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes