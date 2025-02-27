import re

def palindromes_of_specific_lengths(s):
    s = s[103:277].lower()
    set_of_palindromes = set()
    for length in range(100, 170):
        for start in range(len(s) - length + 1):
            candidate = s[start:start + length]
            if candidate == candidate[::-1] and re.match('^[a-z]*$', candidate):
                set_of_palindromes.add(candidate)
    return set_of_palindromes