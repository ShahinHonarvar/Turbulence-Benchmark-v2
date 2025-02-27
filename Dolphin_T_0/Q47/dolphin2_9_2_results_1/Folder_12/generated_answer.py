import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[61:88]
    for length in range(18, 22):
        for i in range(len(substring) - length + 1):
            pal = substring[i:i + length]
            pal = re.sub('[^a-zA-Z]', '', pal)
            if pal.lower() == ''.join(reversed(pal.lower())):
                palindromes.add(pal)
    return palindromes