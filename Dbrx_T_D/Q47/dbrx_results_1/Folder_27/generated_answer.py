import re

def palindromes_of_specific_lengths(s):
    s = s[13:100].lower()
    palindromes = set()
    for i in range(26, 30):
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1] and re.match('[a-zA-Z]*$', s[j:j + i]):
                palindromes.add(s[j:j + i])
    return palindromes