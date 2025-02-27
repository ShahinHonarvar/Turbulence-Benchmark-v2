import re

def return_vowels(s):
    m = re.match('[aieouAEIOU]([jJ]?)', s)
    return m.group(1)