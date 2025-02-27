import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('\\\\W+', '', s)
    s = s.lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 46, length):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes