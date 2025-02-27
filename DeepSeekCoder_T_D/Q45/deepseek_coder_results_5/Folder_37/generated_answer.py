def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[1:5].lower()))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 4, len(letters)):
            word = letters[i:j + 1]
            if len(word) >= 5 and is_palindrome(word):
                palindromes.add(word)
    return palindromes