import re

def palindrome_of_length_at_least_n(s):
    new_s = re.sub('\\W+', '', s)
    new_s = new_s.lower()
    palindromes = set()
    for i in range(len(new_s)):
        for j in range(i + 95, len(new_s)):
            substring = new_s[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes