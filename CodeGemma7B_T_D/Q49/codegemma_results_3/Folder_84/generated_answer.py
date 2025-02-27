def if_decimal_is_divisible(binary):
    dec = int(binary, 2)
    for n in range(len(binary)):
        fib = sum((a + b for a, b in zip(Fibonacci(), Fibonacci()[n:])))
        if dec % fib == 0:
            return True
    return False