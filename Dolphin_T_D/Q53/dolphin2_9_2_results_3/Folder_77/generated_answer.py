from itertools import islice

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(len(s) - 148):
        substring = s[i:i + 149]
        if all((x in alpha for x in substring)) and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes