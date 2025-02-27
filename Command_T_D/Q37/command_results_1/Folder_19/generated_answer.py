import re

def filter_chars(s):
    return re.sub('((?<=\\d)E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T)\\d)', '', s)