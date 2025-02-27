def if_decimal_is_divisible(binary_representation):

    def get_fibonacci_number(n):
        if n in (0, 1):
            return n
        return get_fibonacci_number(n - 1) + get_fibonacci_number(n - 2)

    def get_binary_to_decimal(binary_representation):
        return int(binary_representation, 2)

    def get_nth_fibonacci_divisible_by_number(nth, number):
        while True:
            if get_fibonacci_number(nth) % number == 0:
                return nth
            nth += 1
    nth_fibonacci_divisible_by_number = get_nth_fibonacci_divisible_by_number(1, 135)
    return get_binary_to_decimal(binary_representation) % nth_fibonacci_divisible_by_number == 0