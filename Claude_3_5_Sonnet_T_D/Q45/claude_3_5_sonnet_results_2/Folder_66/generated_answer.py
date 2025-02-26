def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:6] if c.isalpha()]

    def generate_palindromes(chars, length):
        if length <= 0:
            return ['']
        if length == 1:
            return chars
        palindromes = []
        for char in chars:
            for sub_palindrome in generate_palindromes(chars, length - 2):
                palindromes.append(char + sub_palindrome + char)
        return palindromes
    result = set()
    for length in range(5, len(letters) + 1):
        palindromes = generate_palindromes(letters, length)
        result.update(palindromes)
    return result