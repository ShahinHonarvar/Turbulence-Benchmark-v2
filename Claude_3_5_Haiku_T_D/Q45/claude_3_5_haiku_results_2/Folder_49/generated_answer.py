def palindromes_between_indices(s):
    letters = [char.lower() for char in s[5:8] if char.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars):

        def backtrack(current, remaining):
            if len(current) >= 3 and is_palindrome(current):
                result.add(current)
            for i in range(len(remaining)):
                backtrack(current + remaining[i], remaining[:i] + remaining[i + 1:])
        result = set()
        backtrack('', chars)
        return result
    return generate_palindromes(letters)