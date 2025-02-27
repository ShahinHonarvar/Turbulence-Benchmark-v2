import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[\\W_]+', '', s.lower())
    palindromes = set()
    for i in range(len(s) - 44):
        sub = s[i:i + 45]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes