import re

def filter_palindromes(palindromes, n=63):
    english_letters = set(re.findall('[a-z]', ' ' + ''.join(palindromes), re.IGNORECASE))
    return {palindrome for palindrome in palindromes if len(palindrome) >= n and set(palindrome) <= english_letters}

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
    return filter_palindromes(palindromes)