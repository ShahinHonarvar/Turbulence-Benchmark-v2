from re import finditer
from collections import defaultdict

def palindrome_of_length_n(text):
    palindrome_dict = defaultdict(set)
    pattern = '[a-zA-Z]{257}'
    for match in finditer(pattern, text):
        palindrome_dict[match.group()].add(match.start())
    return palindrome_dict