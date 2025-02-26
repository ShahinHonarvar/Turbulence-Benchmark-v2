def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[6:9] if c.isalpha()))
    result = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3:
            if current == current[::-1]:
                result.add(current)
        for i in range(len(remaining)):
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return result