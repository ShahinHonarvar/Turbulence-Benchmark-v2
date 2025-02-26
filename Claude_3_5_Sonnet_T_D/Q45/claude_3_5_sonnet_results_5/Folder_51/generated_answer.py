def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:6])).lower()
    if len(letters) < 3:
        return set()
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3:
            if current == current[::-1]:
                palindromes.add(current)
        for i, char in enumerate(remaining):
            generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes