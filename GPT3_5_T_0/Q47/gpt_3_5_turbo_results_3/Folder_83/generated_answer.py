import re

def palindromes_of_specific_lengths(string):
    substring = string[75:96]
    substring = re.sub('[^a-zA-Z]', '', substring)
    substring = substring.lower()
    palindromes = set()
    for length in range(7, 10):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes