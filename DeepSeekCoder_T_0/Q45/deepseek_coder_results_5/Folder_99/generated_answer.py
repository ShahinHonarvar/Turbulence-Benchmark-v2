def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[4:9])).lower()
    palindromes = set()
    n = len(letters)
    for i in range(n):
        for j in range(i + 2, n):
            substring = letters[i:j + 1]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes