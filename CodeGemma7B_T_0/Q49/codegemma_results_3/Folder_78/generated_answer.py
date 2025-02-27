def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def get_nth_fibonacci(n):
        fib_list = [fibonacci(i) for i in range(n + 1)]
        return fib_list[n]

    def get_decimal_value(binary_str):
        return int(binary_str, 2)
    if get_decimal_value(binary_str) % get_nth_fibonacci(115) == 0:
        return True
    return False