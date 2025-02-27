def palindrome_of_length_n(string):

    def is_palindrome(p):
        return p == p[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(string) - 187):
        substring = string[i:i + 188]
        if all((c in english_letters for c in substring)):
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes