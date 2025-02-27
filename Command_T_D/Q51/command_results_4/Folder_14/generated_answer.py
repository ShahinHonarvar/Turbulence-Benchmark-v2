import collections
import re

def if_contains_anagrams(s):
    if len(s) == 1:
        return False
    elif len(s) == 2:
        if len(s[0]) != len(s[1]):
            return False
        elif s[0] == s[1]:
            return True
        else:
            return False
    elif len(s) == 3:
        if len(s[0]) != len(s[1]) != len(s[2]):
            return False
        elif s[0] == s[1] == s[2]:
            return True
        elif s[0] == s[1]:
            return False
        elif s[1] == s[2]:
            return False
        else:
            return False
    elif len(s) == 4:
        if len(s[0]) != len(s[1]) != len(s[2]) != len(s[3]):
            return False
        elif s[0] == s[1] == s[2] == s[3]:
            return True
        elif s[0] == s[1] == s[3]:
            return False
        elif s[1] == s[2] == s[3]:
            return False
        elif s[0] == s[2] == s[3]:
            return False
        else:
            return False
    else:
        return False