from re import findall, sub

def palindrome_of_length_n(str):
    str = str.lower()
    return set(filter(lambda x: len(x) == 15, findall('(?<![a-z])([a-z]{15})(?![a-z])', str)))