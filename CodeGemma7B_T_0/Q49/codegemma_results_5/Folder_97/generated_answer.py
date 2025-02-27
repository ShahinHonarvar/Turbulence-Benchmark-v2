def if_decimal_is_divisible(binary_str):

    def get_next_fib(num):
        if num in (0, 1):
            return num + 1
        return get_next_fib(get_next_fib(num - 1)) + get_next_fib(num - 2)

    def get_fib_at(index):
        if index in (0, 1):
            return index
        return get_fib_at(index - 1) + get_fib_at(index - 2)

    def get_decimal_from_binary(binary_str):
        return int(binary_str, 2)

    def is_divisible(num, divisor):
        return num % divisor == 0
    binary_int = get_decimal_from_binary(binary_str)
    fib_at_114 = get_fib_at(114)
    return is_divisible(binary_int, fib_at_114)