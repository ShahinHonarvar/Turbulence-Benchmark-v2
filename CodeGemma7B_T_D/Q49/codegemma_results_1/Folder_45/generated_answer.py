def if_decimal_is_divisible(binary):
    Fibonacci = [0]
    n = 1
    while n < len(binary):
        Fibonacci.append(Fibonacci[n - 1] + Fibonacci[n - 2])
        n += 1
    x = int(binary, 2)
    i = 0
    for num in Fibonacci:
        if x % num == 0:
            return True
        i += 1
    return False