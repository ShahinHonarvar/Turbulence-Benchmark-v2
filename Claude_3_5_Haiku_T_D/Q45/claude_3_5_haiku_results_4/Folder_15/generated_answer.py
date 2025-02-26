def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):

        def backtrack(current, remaining):
            if len(current) >= 3 and is_palindrome(current):
                palindrome_set.add(current)
            for i in range(len(remaining)):
                backtrack(current + remaining[i], remaining[:i] + remaining[i + 1:])
        palindrome_set = set()
        backtrack('', letters)
        return palindrome_set
    if len(s) < 3:
        return set()
    letters_in_range = [c.lower() for c in s[1:3] if c.isalpha()]
    if not letters_in_range:
        return set()
    return generate_palindromes(letters_in_range)