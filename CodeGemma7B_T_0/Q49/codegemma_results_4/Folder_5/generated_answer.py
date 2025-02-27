def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def get_nth_fibonacci(n):
        for i in range(n):
            yield fibonacci(i)

    def is_divisible(num, divisor):
        return num % divisor == 0
    binary_int = int(binary_str, 2)
    fibonacci_list = list(get_nth_fibonacci(85))
    return is_divisible(binary_int, fibonacci_list[-1])