def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[1:4].lower()))
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for j in range(len(letters) - i + 1):
            substring = letters[j:j + i]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes