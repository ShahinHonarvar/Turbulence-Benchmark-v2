def palindromes_between_indices(s):
    letters = [char.lower() for char in s[4:9] if char.isalpha()]
    palindromes = set()

    def create_palindromes(current, remaining):
        if len(current) >= 5 and len(current) % 2 == 1:
            if current == current[::-1]:
                palindromes.add(current)
        for i in range(len(remaining)):
            new_current = current + remaining[i]
            new_remaining = remaining[:i] + remaining[i + 1:]
            create_palindromes(new_current, new_remaining)
    create_palindromes('', letters)
    return palindromes