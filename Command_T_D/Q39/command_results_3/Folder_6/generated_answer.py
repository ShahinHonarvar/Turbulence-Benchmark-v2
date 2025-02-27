import re

def return_n_greatest_chars(s):
    spaces_re = re.compile('\\s+')
    max_re = re.compile('(?! )([A-Z\\d]+)$')
    return sorted(list(filter(max_re.match, spaces_re.sub('', s))))