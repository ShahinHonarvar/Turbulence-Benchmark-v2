import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 143):
        for j in range(i + 144, len(s), 142):
            palindrome = s[i:j]
            if palindrome == palindrome[::-1] and re.fullmatch('[a-z]*', palindrome):
                palindromes.add(palindrome)
    if not palindromes:
        return set()
    else:
        return {p for p in palindromes if len(p) == max(map(len, palindromes))}