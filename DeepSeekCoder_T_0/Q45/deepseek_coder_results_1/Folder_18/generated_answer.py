def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[1:7])).lower()
    palindromes = set()
    n = len(letters)
    for i in range(3, n + 1):
        for j in range(n - i + 1):
            substring = letters[j:j + i]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes