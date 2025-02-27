import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = re.sub('\\\\W+', '', s)
    length = len(s)
    set_of_palindromes = set()
    for i in range(length):
        for j in range(i + 8, length):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                set_of_palindromes.add(substring)
    return set_of_palindromes