import re

def filter_chars(s):
    return re.sub('(?i)[%<ixty-one-to-eighty-seven-excl]{%}%< sixty-one-to-eighty-seven-excl]{%}[^q]', '', s)