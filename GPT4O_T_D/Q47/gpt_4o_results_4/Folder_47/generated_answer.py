import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[39:95]
    substring = re.sub('[^a-zA-Z]', '', substring)
    n = len(substring)
    substring = substring.lower()
    for i in range(n):
        for j in range(i + 14, min(i + 53, n + 1)):
            word = substring[i:j]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes