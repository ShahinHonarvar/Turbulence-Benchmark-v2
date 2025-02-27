def if_decimal_is_divisible(binary_str):

    def get_nth_fibonacci(n):
        first, second = (0, 1)
        for _ in range(1, n):
            first, second = (second, first + second)
        return second
    num = int(binary_str, 2)
    nth_fibonacci = get_nth_fibonacci(186)
    return num % nth_fibonacci == 0