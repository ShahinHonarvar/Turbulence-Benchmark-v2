def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[1:6] if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()
    length = len(letters)
    for i in range(length):
        for j in range(i + 6, length + 1):
            substring = letters[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes