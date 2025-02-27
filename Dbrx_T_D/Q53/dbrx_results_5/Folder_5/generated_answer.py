import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('\\W+', ' ', s).lower()
    palindromes = set()
    for i in range(len(s) - 45):
        for j in range(i + 46, len(s), 46):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes