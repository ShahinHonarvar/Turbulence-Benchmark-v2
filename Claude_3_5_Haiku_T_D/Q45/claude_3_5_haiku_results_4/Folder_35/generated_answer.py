def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:5] if c.isalpha()]
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 4 and current == current[::-1]:
            palindromes.add(current)
        for i in range(len(remaining)):
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes