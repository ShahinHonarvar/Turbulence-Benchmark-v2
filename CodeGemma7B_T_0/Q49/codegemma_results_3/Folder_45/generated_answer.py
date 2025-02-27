def if_decimal_is_divisible(binary_str):

    def get_fibonacci(n):
        if n in (0, 1):
            return n
        return get_fibonacci(n - 1) + get_fibonacci(n - 2)

    def get_binary_to_decimal(binary_str):
        return int(binary_str, 2)

    def get_nth_fibonacci_divisible_by_binary(binary_str):
        nth_fibonacci = 0
        while True:
            nth_fibonacci += 1
            if get_fibonacci(nth_fibonacci) % get_binary_to_decimal(binary_str) == 0:
                return nth_fibonacci
    if len(binary_str) == 1 and binary_str == '0':
        return True
    if len(binary_str) == 1 and binary_str == '1':
        return False
    if len(binary_str) > 1 and binary_str[0] == '0':
        return False
    if len(binary_str) > 1 and binary_str[0] == '1':
        return if_decimal_is_divisible(binary_str[1:])
    if len(binary_str) > 2 and binary_str[0:2] == '10':
        return if_decimal_is_divisible(binary_str[2:])
    if len(binary_str) > 2 and binary_str[0:2] == '11':
        return get_nth_fibonacci_divisible_by_binary(binary_str) % 28 == 0