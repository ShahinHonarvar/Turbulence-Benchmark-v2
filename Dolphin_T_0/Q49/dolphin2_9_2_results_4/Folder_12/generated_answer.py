def if_decimal_is_divisible(binary_representation):
    n = 0
    for digit in binary_representation:
        n = n * 2 + int(digit)
    fibs = [0, 1]
    for _ in range(2, 66):
        fibs.append(fibs[-1] + fibs[-2])
    fib66 = fibs[-1]
    return n % fib66 == 0