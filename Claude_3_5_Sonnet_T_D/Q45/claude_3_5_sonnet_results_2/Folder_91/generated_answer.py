def palindromes_between_indices(input_string):
    letters = ''.join((char.lower() for char in input_string[2:7] if char.isalpha()))

    def is_palindrome(s):
        return s == s[::-1]

    def generate_palindromes(chars, length):
        if length <= 2:
            return set()
        palindromes = set()

        def backtrack(current, remaining):
            if len(current) == length:
                if is_palindrome(current):
                    palindromes.add(current)
                return
            for i, char in enumerate(remaining):
                backtrack(current + char, remaining[:i] + remaining[i + 1:])
        backtrack('', chars)
        return palindromes
    result = set()
    for length in range(3, len(letters) + 1):
        result.update(generate_palindromes(letters, length))
    return result