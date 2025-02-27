import collections
import re

def if_contains_anagrams(s):
    table = collections.Counter(s)
    if not all((table[k] == 1 for k in table)):
        return False
    s = re.sub('([A-Z])([a-z])([A-Z])', '\x01\x02\x03', s)
    if len(s) < 3:
        return False
    if table[s]:
        return False
    return True