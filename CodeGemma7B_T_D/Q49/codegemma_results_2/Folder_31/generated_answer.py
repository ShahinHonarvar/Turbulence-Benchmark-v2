def if_decimal_is_divisible(bin_str):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def nth_fibonacci(n):
        if n < 0:
            return None
        else:
            fib_nums = [fibonacci(i) for i in range(n + 1)]
            return fib_nums[-1]
    nth_69th_num = nth_fibonacci(68)
    _int = int(bin_str, 2)
    if _int % nth_69th_num == 0:
        return True
    else:
        return False