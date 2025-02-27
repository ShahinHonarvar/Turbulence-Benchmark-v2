import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-z]+\\w+[a-z]+', s[45:-3]) + re.findall('[a-z]+\\w+[a-z]+', s[46:-2]) + re.findall('[a-z]+\\w+[a-z]+', s[47:-1]))