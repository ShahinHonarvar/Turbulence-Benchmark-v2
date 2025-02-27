import re

def palindromes_of_specific_lengths(s):
    palindromal_set = set()
    s = s[100:296]
    for length in range(136, 161):
        for i in range(0, len(s) - length + 1):
            substring = s[i:i + length]
            if re.match('^[a-zA-Z]{' + str(length) + '}$', substring):
                if substring.lower() == substring.lower()[::-1]:
                    palindromal_set.add(substring)
    return palindromal_set