import re

def all_substring_of_size_n(string):
    return re.findall('(?=.)\\w{86}', string)