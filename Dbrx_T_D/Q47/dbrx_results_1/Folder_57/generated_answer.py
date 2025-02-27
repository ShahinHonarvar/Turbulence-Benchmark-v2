import re

def palindromes_of_specific_lengths(s):
    pallist = set()
    for length in range(39, 53):
        for i in range(16, len(s) - length + 1):
            if re.match('^[a-zA-Z]*$', s[i:i + length]):
                if s[i:i + length].lower() == s[i:i + length][::-1].lower():
                    pallist.add(s[i:i + length])
    return pallist