def palindrome_of_length_n(string):

    def is_palindrome(string):
        return string == string[::-1]
    palindromes = set()
    for i in range(len(string) - 420 + 1):
        for j in range(i + 420, len(string) + 1):
            substring = string[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes