def if_decimal_is_divisible(binary):
    fib = [0, 1]
    a = b = c = 0
    for i in range(binary.__len__()):
        a = b
        b = c
        c = a + b
        fib.append(c)
    n1 = int(binary, 2)
    n2 = int(str(fib[-78]), 0)
    if n1 % n2 == 0:
        return True
    return False