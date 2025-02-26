def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[4:10] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 2:
            return set()
        result = set()

        def backtrack(current, remaining):
            if len(current) == length:
                if is_palindrome(current):
                    result.add(current)
                return
            for i, char in enumerate(remaining):
                backtrack(current + char, remaining[:i] + remaining[i + 1:])
        backtrack('', chars)
        return result
    palindromes = set()
    for length in range(3, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return palindromes