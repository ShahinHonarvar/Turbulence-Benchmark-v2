def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:7] if c.isalpha()]
    result = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 4:
            if current == current[::-1]:
                result.add(current)
        for i in range(len(remaining)):
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return result