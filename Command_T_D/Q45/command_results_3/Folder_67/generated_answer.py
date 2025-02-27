import re

def palindromes_between_indices(str):
    str = re.sub('[^a-z0-9]+', '', str)
    return set(re.findall('(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])' + str, str))