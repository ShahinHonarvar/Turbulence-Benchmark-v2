import re

def palindromes_between_indices(s):
    s = re.sub('[^A-Za-z]+', '', s)
    if not s:
        return set()
    return set(re.findall('((?=([a-z]))[a-z]{1})((?=([a-z]))[a-z]{5})', s))