def if_decimal_is_divisible(bin_string):
    decimal_number = int(bin_string, 2)

    def nth_fibonacci(n):
        a = 0
        b = 1
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_num = nth_fibonacci(105)
    if decimal_number % fib_num == 0:
        return True
    else:
        return False