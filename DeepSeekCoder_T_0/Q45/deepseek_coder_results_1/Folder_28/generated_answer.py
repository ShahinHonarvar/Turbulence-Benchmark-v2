def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[1:6].lower()))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 4, len(letters) + 1):
            substring = letters[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes