def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:7] if c.isalpha()]
    result = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 6:
            if current == current[::-1]:
                result.add(current)
        if remaining:
            for i, char in enumerate(remaining):
                generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return result