def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:9] if char.isalpha()]
    if len(letters) < 6:
        return set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(available_letters):

        def backtrack(current, remaining):
            if len(current) >= 6 and is_palindrome(current):
                palindromes.add(current)
            for i in range(len(remaining)):
                new_current = current + remaining[i]
                new_remaining = remaining[:i] + remaining[i + 1:]
                backtrack(new_current, new_remaining)
        palindromes = set()
        backtrack('', available_letters)
        return palindromes
    return generate_palindromes(letters)