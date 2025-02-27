def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(string):
    n = 45
    string = ''.join(filter(str.isalpha, string)).lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + n, len(string) + 1):
            if is_palindrome(string[i:j]):
                palindromes.add(string[i:j])
    return palindromes