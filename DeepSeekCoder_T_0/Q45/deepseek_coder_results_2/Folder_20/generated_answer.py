def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[2:9].lower()))
    palindromes = set()
    n = len(letters)
    for i in range(n):
        for j in range(i + 4, n + 1):
            if is_palindrome(letters[i:j]):
                palindromes.add(letters[i:j])
    return palindromes