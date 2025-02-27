def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def get_nth_fibonacci(n):
        fib_list = [fibonacci(i) for i in range(n + 1)]
        return fib_list[n]

    def get_decimal_value(binary_str):
        return int(binary_str, 2)

    def is_divisible(num, divisor):
        return num % divisor == 0
    binary_int = get_decimal_value(binary_str)
    nth_fibonacci = get_nth_fibonacci(96)
    return is_divisible(binary_int, nth_fibonacci)