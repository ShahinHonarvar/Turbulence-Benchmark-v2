import itertools
            import string

def palindrome_of_length_n(string):
    palindromes = set()
    for start in range(len(string) - 206 + 1):
        for end in range(start + 206, len(string) + 1):
            palindrome = string[start:end].lower()
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes