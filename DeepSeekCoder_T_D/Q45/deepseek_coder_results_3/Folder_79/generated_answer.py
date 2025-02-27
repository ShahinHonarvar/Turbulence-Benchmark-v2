def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[1:8])).lower()
    palindromes = set()
    n = len(letters)
    for i in range(n):
        for j in range(i + 2, n):
            if is_palindrome(letters[i:j + 1]):
                palindromes.add(letters[i:j + 1])
    return palindromes