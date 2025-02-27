import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(106, 281):
        for j in range(136, 152):
            if i + j >= 280:
                break
            palindrome = string[i:i + j].lower()
            if re.fullmatch('[a-z]*', palindrome) and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes