def palindrome_of_length_at_least_n(word):
    """Finds all palindromes of the length greater than or equal to 112 that exist in the given string.
    Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner."""

    def is_palindrome(string):
        """Checks if the given string is a palindrome."""
        return string == string[::-1]

    def generate_palindromes(word, start, end):
        """Generates all palindromes of the length greater than or equal to 112 that exist in the given string."""
        palindromes = set()
        for i in range(start, end):
            for j in range(i + 1, end + 1):
                substring = word[i:j]
                if len(substring) >= 112 and is_palindrome(substring):
                    palindromes.add(substring)
        return palindromes
    all_palindromes = set()
    for i in range(len(word)):
        palindromes = generate_palindromes(word.lower(), i, len(word))
        all_palindromes.update(palindromes)
    return all_palindromes