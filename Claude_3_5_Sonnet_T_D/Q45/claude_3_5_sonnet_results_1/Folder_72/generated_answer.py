def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[1:8] if c.isalpha()))

    def generate_palindromes(chars, current='', left='', right=''):
        if len(current) >= 6 and current == current[::-1]:
            palindromes.add(current)
        if chars:
            for i, c in enumerate(chars):
                generate_palindromes(chars[:i] + chars[i + 1:], current + c, left + c, c + right)
                if len(current) >= 2:
                    generate_palindromes(chars[:i] + chars[i + 1:], left + c + right)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes