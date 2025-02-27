def if_decimal_is_divisible(binary_str):

    def get_next_fibonacci(num):
        if num in (0, 1):
            return num
        return get_next_fibonacci(num - 1) + get_next_fibonacci(num - 2)

    def get_binary_value(binary_str):
        return int(binary_str, 2)

    def is_divisible(num, divisor):
        return num % divisor == 0
    fibonacci_num = get_next_fibonacci(186)
    binary_int = get_binary_value(binary_str)
    return is_divisible(binary_int, fibonacci_num)