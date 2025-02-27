def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    letters = ''.join((c for c in s[3:10] if c.isalpha())).lower()
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes