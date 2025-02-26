def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:6] if c.isalpha()]
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(remaining) == 0 and len(current) >= 5 and (current == current[::-1]):
            palindromes.add(current)
            return
        for i in range(len(remaining)):
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes