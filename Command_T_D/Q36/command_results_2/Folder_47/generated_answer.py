import re

def filter_chars(s):
    return re.sub('[^A-Ga-g][^D-f][^g-i][^j-n]', '', s)