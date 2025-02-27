import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    regex = '\\b[a-z]{26,}\\b'
    palindromes = set()
    for match in re.findall(regex, s):
        for i in range(len(match)):
            for j in range(i + 26, len(match) + 1):
                substring = match[i:j]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes