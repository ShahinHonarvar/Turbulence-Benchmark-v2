def if_decimal_is_divisible(binary_str):

    def get_next_fib(num):
        if num in (0, 1):
            return num
        return get_next_fib(num - 1) + get_next_fib(num - 2)

    def get_decimal_from_binary(binary_str):
        return int(binary_str, 2)

    def is_divisible(num, divisor):
        return num % divisor == 0
    fib_num = get_next_fib(169)
    decimal = get_decimal_from_binary(binary_str)
    return is_divisible(decimal, fib_num)