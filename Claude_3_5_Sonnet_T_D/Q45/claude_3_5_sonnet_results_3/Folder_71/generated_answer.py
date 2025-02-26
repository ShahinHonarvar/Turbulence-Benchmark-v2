def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:4] if c.isalpha()]

    def generate_palindromes(current, remaining):
        if len(current) >= 4:
            if current == current[::-1]:
                palindromes.add(current)
        for i, char in enumerate(remaining):
            generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
            generate_palindromes(char + current, remaining[:i] + remaining[i + 1:])
    palindromes = set()
    generate_palindromes('', letters)
    return palindromes