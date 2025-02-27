import re

def palindromes_between_indices(s):
    s = s[4:-8]
    return set(re.findall('((?P<i>.{5,})(?P<j>.{1,}))\x01(?P<k>.{1,}))\x02(?P=i)\x03(?P=j)\x04(?P=k)', s.lower()))