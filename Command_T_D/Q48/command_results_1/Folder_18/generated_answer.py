import re

def return_binary_or_hexa(test_tup):
    a, b = (test_tup[56], test_tup[90])
    return re.sub('0+$', '', f'{sum((x for x in range(a + 1, b)))}'[::-1])