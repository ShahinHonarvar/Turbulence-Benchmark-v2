def f(n):
    a, b = (0, 1)
    fnums = [a]
    for i in range(n):
        a, b = (b, a + b)
        fnums.append(a)
    return fnums[-1]

def if_decimal_is_divisible(string):
    btoint = int(string, 2)
    cit = 0
    for i in range(42):
        if f(i) > btoint:
            cit = i - 1
            break
    if btoint % f(cit) == 0:
        return True
    else:
        return False