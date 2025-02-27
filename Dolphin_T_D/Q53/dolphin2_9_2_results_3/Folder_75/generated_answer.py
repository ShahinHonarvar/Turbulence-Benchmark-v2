import re

def palindrome_of_length_at_least_n(M):
    M = M.lower()
    return set(re.findall('[a-z]{40,}', M))