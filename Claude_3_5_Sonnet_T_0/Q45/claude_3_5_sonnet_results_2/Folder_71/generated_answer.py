def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:4])).lower()
    result = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 4:
            if current == current[::-1]:
                result.add(current)
        for i, char in enumerate(remaining):
            generate_palindromes(current + char, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return result