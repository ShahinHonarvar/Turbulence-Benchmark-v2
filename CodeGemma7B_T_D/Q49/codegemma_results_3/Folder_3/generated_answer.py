def if_decimal_is_divisible(str):
    l = [int(i) for i in str]
    m = 1
    n = 1
    i = 0
    lc = len(l)
    lb = None
    while lb == None or lb < 35:
        lb = n + m
        if lb >= 35:
            if lb == 35 and lc != i + 1:
                return True
            else:
                return False
        i += 1
        m, n = (n, m + n)