def palindromes_between_indices(string):
    letters = [c.lower() for c in string[3:9] if c.isalpha()]
    result = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 7:
            if current == current[::-1]:
                result.add(current)
        for i, char in enumerate(remaining):
            generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return result