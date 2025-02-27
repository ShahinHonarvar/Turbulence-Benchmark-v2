def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def get_nth_fibonacci(n):
        fib_list = [fibonacci(i) for i in range(n + 1)]
        return fib_list[n]

    def get_decimal_value(binary_str):
        return int(binary_str, 2)

    def is_divisible(num, divisor):
        return num % divisor == 0
    nth_fibonacci = get_nth_fibonacci(159)
    decimal_value = get_decimal_value(binary_str)
    return is_divisible(decimal_value, nth_fibonacci)