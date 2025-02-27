import re

def filter_chars(str1):
    str1 = str1[:4] + str1[5:-8] + str1[-8:]
    return re.sub('(?<=.)([A-J])', '', str1)