import itertools
import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 472, len(s) + 1):
            substring = s[i:j]
            if all((a == b for a, b in zip(substring, reversed(substring)))):
                palindromes.add(substring)
    return palindromes