def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:8] if c.isalpha()]

    def generate_palindromes(chars, current='', left='', right=''):
        if len(current) >= 6 and current == current[::-1]:
            palindromes.add(current)
        if chars:
            for i, c in enumerate(chars):
                generate_palindromes(chars[:i] + chars[i + 1:], current + c, left, right)
                generate_palindromes(chars[:i] + chars[i + 1:], current, left + c, c + right)
        elif left or right:
            generate_palindromes([], left + current + right)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes