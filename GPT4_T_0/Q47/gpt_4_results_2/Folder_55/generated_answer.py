import re

def palindromes_of_specific_lengths(s):
    s = s[10:76]
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 10, i + 21):
            if j > len(s):
                break
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes