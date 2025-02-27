def if_decimal_is_divisible(binary_str):

    def fib_35():
        fib = [0, 1]
        while True:
            fib.append(fib[-1] + fib[-2])
            if fib[-1] > 35:
                break
        return fib
    fib_nums = fib_35()
    decimal = int(binary_str, 2)
    for num in fib_nums:
        if decimal % num == 0:
            return True
    return False