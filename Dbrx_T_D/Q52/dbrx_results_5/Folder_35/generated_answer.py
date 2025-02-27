def is_palindrome(string):
    return string == string[::-1]

def palindrome_of_length_n(string, n=116):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    palindromes = {string[i:j] for i in range(len(string)) for j in range(i + n, len(string) + 1) if is_palindrome(string[i:j])}
    return palindromes