def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[5:7])).lower()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 2:
            return set()
        result = set()

        def backtrack(current, remaining):
            if len(current) >= 3 and is_palindrome(current):
                result.add(current)
            if len(current) == length:
                return
            for i, char in enumerate(remaining):
                backtrack(current + char, remaining[:i] + remaining[i + 1:])
        for l in range(3, len(chars) + 1):
            backtrack('', chars)
        return result
    return generate_palindromes(letters, len(letters))