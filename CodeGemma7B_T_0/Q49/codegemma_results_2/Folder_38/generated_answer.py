def if_decimal_is_divisible(binary_representation):

    def get_fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return get_fibonacci(n - 1) + get_fibonacci(n - 2)

    def get_binary_to_decimal(binary_representation):
        decimal = 0
        for i, bit in enumerate(binary_representation):
            decimal += int(bit) * 2 ** i
        return decimal

    def get_next_fibonacci_divisible_by_78(current_fibonacci):
        while True:
            current_fibonacci += get_fibonacci(len(str(current_fibonacci)))
            if current_fibonacci % 78 == 0:
                return current_fibonacci
    binary_to_decimal = get_binary_to_decimal(binary_representation)
    next_fibonacci_divisible_by_78 = get_next_fibonacci_divisible_by_78(binary_to_decimal)
    return next_fibonacci_divisible_by_78 % binary_to_decimal == 0