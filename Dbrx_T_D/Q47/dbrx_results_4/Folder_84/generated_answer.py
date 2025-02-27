from collections import defaultdict

def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(13, 41):
        for index in range(23, 78 - length + 1):
            if all((char in english_letters for char in s[index:index + length])):
                palindrome = s[index:index + length]
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome.lower())
    return palindromes