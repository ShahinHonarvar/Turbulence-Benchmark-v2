def if_decimal_is_divisible(binary_representation):
    n = int(binary_representation, 2)
    fib47 = [0, 1]
    for i in range(2, 48):
        fib47.append(fib47[i - 1] + fib47[i - 2])
    if n % fib47[47] == 0:
        return True
    else:
        return False