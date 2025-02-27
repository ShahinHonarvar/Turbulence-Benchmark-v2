import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('\\W+', '', s).lower()
    set_palindrome = set()
    for i in range(25, len(s) + 1):
        for j in range(0, len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1]:
                set_palindrome.add(substring)
    return set_palindrome