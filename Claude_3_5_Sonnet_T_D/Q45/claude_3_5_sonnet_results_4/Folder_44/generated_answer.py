def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:8] if c.isalpha()]
    result = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3:
            if current == current[::-1]:
                result.add(current)
        if len(current) < len(letters):
            for i, char in enumerate(remaining):
                generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return result