def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:8] if c.isalpha()]
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 5 and len(current) % 2 == 1:
            mid = current[len(current) // 2]
            left = current[:len(current) // 2]
            if current == left + mid + left[::-1]:
                palindromes.add(current)
        for i in range(len(remaining)):
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes