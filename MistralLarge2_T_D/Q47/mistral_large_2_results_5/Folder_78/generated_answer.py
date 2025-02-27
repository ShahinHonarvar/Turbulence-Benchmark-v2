import re

def palindromes_of_specific_lengths(s):
    s = s[15:73]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    palindromes = set()
    for length in range(19, 56):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes