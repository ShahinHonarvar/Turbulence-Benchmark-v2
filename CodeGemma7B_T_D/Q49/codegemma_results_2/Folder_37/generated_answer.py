def if_decimal_is_divisible(binary_representation):
    fibn = {0: 0, 1: 1}
    fib = 0
    j = 1
    while fib < 46:
        fib = fibn[j - 1] + fibn[j - 2]
        fibn[j] = fib
        j += 1
    i = 0
    num = 0
    while i < len(binary_representation):
        num = num * 2 + int(binary_representation[i])
        i += 1
    if num % fib == 0:
        return True
    else:
        return False