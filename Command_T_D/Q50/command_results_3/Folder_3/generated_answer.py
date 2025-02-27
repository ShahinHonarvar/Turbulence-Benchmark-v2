import re

def if_contains_anagrams(list):
    return bool(re.findall('\\A[a-z]{3}([a-z]{%d}\x01){2}\\Z' % (len(list), list), list))