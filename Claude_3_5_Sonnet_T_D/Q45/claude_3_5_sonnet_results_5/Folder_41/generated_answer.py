def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:4])).lower()
    if len(letters) < 2:
        return set()
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3:
            if current == current[::-1]:
                palindromes.add(current)
        for i in range(len(remaining)):
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes