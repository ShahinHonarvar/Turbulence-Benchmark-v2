import re

def palindromes_of_specific_lengths(s):
    s = s[10:60].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 18, i + 37):
            if j > len(s):
                break
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes