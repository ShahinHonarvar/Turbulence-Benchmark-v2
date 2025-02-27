import re

def filter_chars(s):
    return re.sub('([\\d\\w])([\\d\\w]38[\\d\\w]81[\\d\\w])([\\d\\w])', '\x01.\x02.\x03', s)