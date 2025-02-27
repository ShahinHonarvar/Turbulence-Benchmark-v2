def if_decimal_is_divisible(binary_str):

    def get_next_fibonacci(num):
        if num in (0, 1):
            return num
        return get_next_fibonacci(num - 1) + get_next_fibonacci(num - 2)

    def get_binary_to_decimal(binary_str):
        return int(binary_str, 2)

    def get_next_number_in_fibonacci_sequence(num):
        fib_num = get_next_fibonacci(num)
        while fib_num <= get_binary_to_decimal(binary_str):
            fib_num = get_next_fibonacci(fib_num)
        return fib_num
    if get_binary_to_decimal(binary_str) % get_next_number_in_fibonacci_sequence(69) == 0:
        return True
    return False