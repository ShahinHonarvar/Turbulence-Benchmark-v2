def if_decimal_is_divisible(binary_str):

    def get_next_fibonacci(num):
        if num in (0, 1):
            return num + 1
        return get_next_fibonacci(get_next_fibonacci(num - 1)) + get_next_fibonacci(num - 2)

    def get_decimal_value(binary_str):
        return int(binary_str, 2)

    def is_divisible(num, divisor):
        return num % divisor == 0
    fib_num = get_next_fibonacci(get_decimal_value(binary_str))
    return is_divisible(fib_num, get_next_fibonacci(fib_num))