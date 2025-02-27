def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[0:6].lower()))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            if is_palindrome(letters[i:j]):
                palindromes.add(letters[i:j])
    return palindromes