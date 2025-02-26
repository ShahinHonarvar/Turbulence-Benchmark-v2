def palindromes_between_indices(string):
    letters = [char.lower() for char in string[3:9] if char.isalpha()]
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 7 and len(current) % 2 == 1:
            mid = len(current) // 2
            if current[:mid] == current[mid + 1:][::-1]:
                palindromes.add(current)
        for i in range(len(remaining)):
            if i > 0 and remaining[i] == remaining[i - 1]:
                continue
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes