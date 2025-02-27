import re

def palindromes_of_specific_lengths(s):
    s = s[10:60].lower()
    palindromes = set()
    for i in range(len(s) - 17):
        for j in range(18, 37):
            if s[i:i + j] == s[i:i + j][::-1] and re.match('[a-zA-Z]' * j, s[i:i + j]):
                palindromes.add(s[i:i + j])
    return palindromes