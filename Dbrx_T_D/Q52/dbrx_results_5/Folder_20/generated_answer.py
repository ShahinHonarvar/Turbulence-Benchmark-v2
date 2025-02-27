import re

def palindrome_of_length_n(s):
    n = 53
    alpha_only = re.findall('\\b\\w+\\b', s, re.IGNORECASE)
    palindromes = set()
    for i in range(len(alpha_only) - n + 1):
        if alpha_only[i:i + n][::-1] == alpha_only[i:i + n]:
            palindromes.add(''.join(alpha_only[i:i + n]))
    if not palindromes:
        palindromes.add('')
    return palindromes