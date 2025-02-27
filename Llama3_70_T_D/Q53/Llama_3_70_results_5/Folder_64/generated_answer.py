import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    words = re.findall('\\\\b[a-z]+\\\\b', s)
    palindromes = set()
    for word in words:
        for length in range(9, len(word) + 1):
            for i in range(len(word) - length + 1):
                substring = word[i:i + length]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes