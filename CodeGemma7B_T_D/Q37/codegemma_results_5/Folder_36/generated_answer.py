from string import ascii_lowercase
from string import ascii_uppercase

def filter_chars(s):
    for i in range(259, 503):
        if s[i] in ascii_lowercase or s[i] in ascii_uppercase:
            if s[i] >= ',' and s[i] <= '3':
                s = s.replace(s[i], '')
    return s