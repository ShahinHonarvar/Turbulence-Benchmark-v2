import re

def palindromes_of_specific_lengths(s):
    s = s.lower()
    length_range = range(23, 39)
    index_range = range(41, 90)
    palindromes = set()
    for i in index_range:
        for length in length_range:
            if i + length <= len(s) and s[i:i + length] == s[i:i + length][::-1]:
                palindromes.add(s[i:i + length])
    palindromes = {palindrome for palindrome in palindromes if re.match('^[a-zA-Z]*$', palindrome)}
    return palindromes