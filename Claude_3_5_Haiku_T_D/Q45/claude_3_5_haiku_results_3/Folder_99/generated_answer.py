def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):

        def backtrack(path, remaining):
            if len(path) >= 3 and is_palindrome(path):
                result.add(path)
            for i in range(len(remaining)):
                backtrack(path + remaining[i], remaining[:i] + remaining[i + 1:])
        result = set()
        backtrack('', letters)
        return result
    letters = [char.lower() for char in s[4:9] if char.isalpha()]
    palindrome_set = set()
    for length in range(3, len(letters) + 1):
        for combo in generate_palindromes(letters):
            if len(combo) == length:
                palindrome_set.add(combo)
    return palindrome_set