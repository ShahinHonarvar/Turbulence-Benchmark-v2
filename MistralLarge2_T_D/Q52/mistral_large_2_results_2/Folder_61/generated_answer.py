def palindrome_of_length_n(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    n = 74
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes