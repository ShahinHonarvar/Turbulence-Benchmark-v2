def palindromes_between_indices(s):
    letters = [char.lower() for char in s[4:7] if char.isalpha()]
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3 and len(remaining) == 0:
            if current == current[::-1]:
                palindromes.add(current)
            return
        for i in range(len(remaining)):
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes