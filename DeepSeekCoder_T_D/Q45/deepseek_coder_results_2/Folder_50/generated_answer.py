def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[4:9].lower()))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 4, len(letters)):
            substring = letters[i:j + 1]
            if len(substring) >= 5 and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes