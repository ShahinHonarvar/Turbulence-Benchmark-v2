def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:6] if char.isalpha()]
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3 and len(current) % 2 == 1:
            mid = len(current) // 2
            if current == current[:mid] + current[mid] + current[mid::-1]:
                palindromes.add(current)
        for i in range(len(remaining)):
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes