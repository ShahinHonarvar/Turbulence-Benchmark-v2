def palindromes_between_indices(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    letters = [c for c in s[:8] if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes