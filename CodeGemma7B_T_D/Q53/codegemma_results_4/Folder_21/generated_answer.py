import re

def palindrome_of_length_at_least_n(s):
    pattern = '(?=([a-zA-Z])(?=[a-zA-Z]\\\\1)(?=[a-zA-Z]\\\\2)(?=[a-zA-Z]\\\\3)(?=[a-zA-Z]\\\\4)(?=[a-zA-Z]\\\\5)(?=[a-zA-Z]\\\\6)(?=[a-zA-Z]\\\\7)(?=[a-zA-Z]\\\\8)(?=[a-zA-Z]\\\\9)(?=[a-zA-Z]\\\\10)(?=[a-zA-Z]\\\\11)(?=[a-zA-Z]\\\\12))(.*[a-zA-Z]){112,}$'
    s = s.lower()
    return set(re.findall(pattern, s))