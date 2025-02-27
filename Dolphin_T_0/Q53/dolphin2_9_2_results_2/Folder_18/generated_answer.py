import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('\\\\W+', '', s).lower()
    palindromes = set()
    for i in range(62, len(s) + 1):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes