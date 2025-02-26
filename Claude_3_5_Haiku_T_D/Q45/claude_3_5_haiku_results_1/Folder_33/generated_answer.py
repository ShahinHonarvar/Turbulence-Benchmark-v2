def palindromes_between_indices(s):
    letters = [char.lower() for char in s[7:10] if char.isalpha()]
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 4 and len(current) % 2 == 0:
            if current == current[::-1]:
                palindromes.add(current)
        for i in range(len(remaining)):
            new_current = current + remaining[i]
            new_remaining = remaining[:i] + remaining[i + 1:]
            generate_palindromes(new_current, new_remaining)
    generate_palindromes('', letters)
    return palindromes