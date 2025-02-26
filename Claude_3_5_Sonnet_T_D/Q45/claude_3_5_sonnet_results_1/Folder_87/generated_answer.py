def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[3:10] if c.isalpha()))
    n = len(letters)
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3:
            if current == current[::-1]:
                palindromes.add(current)
        if remaining:
            for i, char in enumerate(remaining):
                generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes