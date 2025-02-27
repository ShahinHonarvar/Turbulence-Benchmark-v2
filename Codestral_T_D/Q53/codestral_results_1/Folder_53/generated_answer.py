import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for length in range(64, len(s) + 1):
        for i in range(len(s) - length + 1):
            sub_string = s[i:i + length]
            if sub_string == sub_string[::-1] and re.match('^[a-z]*$', sub_string):
                palindromes.add(sub_string)
    return palindromes