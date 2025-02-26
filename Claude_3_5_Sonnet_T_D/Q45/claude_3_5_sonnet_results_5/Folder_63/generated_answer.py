def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:4] if c.isalpha()]
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3:
            if current == current[::-1]:
                palindromes.add(current)
        for i, char in enumerate(remaining):
            generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes