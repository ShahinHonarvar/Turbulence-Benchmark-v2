def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[:8] if c.isalpha()))
    result = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 4 and current == current[::-1]:
            result.add(current)
        if len(current) >= 8:
            return
        for i in range(len(remaining)):
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return result