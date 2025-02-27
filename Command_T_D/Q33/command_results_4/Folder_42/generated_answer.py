import re

def return_vowels(s):
    m = re.match('[aieou][^;]*[aieou]', s[12:-1])
    if m:
        return list(m.group())
    else:
        return []