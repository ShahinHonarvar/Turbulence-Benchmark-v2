import re

def all_left_right_truncatable_prime(lim):
    res = []
    for a in range(2, int(str(lim)[-1] + '0') + 1):
        x = str(a)
        while x != '1' and x != '11':
            if re.match('^1\x01\\d+\x01\x01$', x):
                res.append(a)
            x = re.match('\\d+', x).group()
    return res