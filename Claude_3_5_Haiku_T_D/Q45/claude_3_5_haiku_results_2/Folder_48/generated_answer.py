def palindromes_between_indices(s):
    letters = [c.lower() for c in s[6:9] if c.isalpha()]
    result = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 4 and len(remaining) == 0:
            if current == current[::-1]:
                result.add(current)
            return
        for i in range(len(remaining)):
            new_current = current + remaining[i]
            new_remaining = remaining[:i] + remaining[i + 1:]
            generate_palindromes(new_current, new_remaining)
            generate_palindromes(remaining[i] + current, new_remaining)
    generate_palindromes('', letters)
    return result