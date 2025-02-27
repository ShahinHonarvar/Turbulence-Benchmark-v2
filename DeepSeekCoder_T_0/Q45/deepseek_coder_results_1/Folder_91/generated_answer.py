def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[2:7])).lower()
    palindromes = set()
    n = len(letters)
    for i in range(n):
        for j in range(i + 2, n + 1):
            substring = letters[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes