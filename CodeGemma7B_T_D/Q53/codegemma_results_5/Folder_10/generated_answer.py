import re

def palindrome_of_length_at_least_n(word):
    """
            description:
            """
    return set(filter(lambda x: len(x) >= 92, re.findall('(?i)\\\\b([a-zA-Z]+\\\\b)\\\\b([a-zA-Z]+\\\\b)', word)))