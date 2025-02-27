def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[4:8].lower()))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 4, len(letters) + 1):
            if j - i >= 5 and is_palindrome(letters[i:j]):
                palindromes.add(letters[i:j])
    return palindromes