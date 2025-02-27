def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[2:4] if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substr = letters[i:i + length]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes