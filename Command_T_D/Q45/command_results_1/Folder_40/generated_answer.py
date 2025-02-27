import re

def palindromes_between_indices(s):
    idx = 4
    end = 9
    while idx < end:
        match = re.fullmatch('[a-z]+', s[idx:end])
        if match:
            idx += match.end()
            end = idx
            break
    return set(re.findall('([a-z]+)[a-z]+', s[idx:end]))