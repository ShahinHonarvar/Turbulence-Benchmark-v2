def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[0:5].lower()))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 4, len(letters) + 1):
            substring = letters[i:j]
            if len(substring) >= 4 and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes