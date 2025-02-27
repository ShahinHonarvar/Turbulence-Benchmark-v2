import re

def remove_repeat_chars(s):
    idx = 0
    while idx < 8:
        for c in s[idx]:
            s = re.sub(f'{c}+', '', s)
        idx += 1
    return s