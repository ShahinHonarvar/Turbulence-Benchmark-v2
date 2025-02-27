import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('\\\\W+', '', s).lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            possible_pal = s[i:j]
            if possible_pal == possible_pal[::-1] and len(possible_pal) >= 22:
                palindromes.add(possible_pal)
    return palindromes