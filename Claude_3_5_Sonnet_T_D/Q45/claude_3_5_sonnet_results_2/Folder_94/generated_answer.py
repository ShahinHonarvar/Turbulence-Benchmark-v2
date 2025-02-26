def palindromes_between_indices(s):
    letters = set((c.lower() for c in s[3:5] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 2:
            return set()
        palindromes = set()
        for char in chars:
            if length == 3:
                palindromes.add(char + char + char)
            else:
                for middle in generate_palindromes(chars, length - 2):
                    palindromes.add(char + middle + char)
        return palindromes
    result = set()
    for length in range(3, len(letters) * 2 + 1):
        result.update(generate_palindromes(letters, length))
    return result