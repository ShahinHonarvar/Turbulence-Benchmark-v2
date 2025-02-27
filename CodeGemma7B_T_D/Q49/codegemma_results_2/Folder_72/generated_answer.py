def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n in (0, 1):
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    decimal_int = int(binary_string, 2)
    for i in range(2, 1000):
        if fibonacci(i) >= decimal_int + fibonacci(i - 1):
            if not decimal_int == 0 and fibonacci(i) % decimal_int == 0:
                return True
    return False