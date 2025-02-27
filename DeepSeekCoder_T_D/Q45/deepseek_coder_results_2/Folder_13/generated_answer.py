def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[3:10].lower()))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 4, len(letters)):
            if j - i >= 4 and is_palindrome(letters[i:j + 1]):
                palindromes.add(letters[i:j + 1])
    return palindromes