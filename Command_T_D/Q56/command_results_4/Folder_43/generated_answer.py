import re

def all_substring_of_size_n(s):
    return [m.group() for m in re.finditer('(?=({}){86}({}))'.format('[a-z]', re.escape(s)), s)]