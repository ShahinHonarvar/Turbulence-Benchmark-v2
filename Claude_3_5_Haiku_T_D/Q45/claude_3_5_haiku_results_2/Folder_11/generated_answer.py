def palindromes_between_indices(s):
    letters = [ch.lower() for ch in s[3:8] if ch.isalpha()]
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 4 and len(current) == len(remaining) * 2:
            if current == current[::-1]:
                palindromes.add(current)
            return
        for i in range(len(remaining)):
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes