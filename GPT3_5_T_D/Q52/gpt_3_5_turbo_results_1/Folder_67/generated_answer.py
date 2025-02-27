import re

def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 41):
        substr = string[i:i + 42]
        substr = re.sub('[^a-zA-Z]', '', substr).lower()
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes