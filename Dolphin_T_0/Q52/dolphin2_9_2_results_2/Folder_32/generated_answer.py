import re

def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 112):
        subs = string[i:i + 113]
        if re.match('^[a-zA-Z]*$', subs) and subs.lower() == subs.lower()[::-1]:
            palindromes.add(subs)
    return palindromes