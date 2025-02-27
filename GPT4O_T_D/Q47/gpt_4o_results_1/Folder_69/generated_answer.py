import re

def palindromes_of_specific_lengths(s):
    s = s[11:97].lower()
    letter_str = re.sub('[^a-z]', '', s)
    palindromes = set()
    for length in range(45, 53):
        for start in range(len(letter_str) - length + 1):
            substring = letter_str[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes