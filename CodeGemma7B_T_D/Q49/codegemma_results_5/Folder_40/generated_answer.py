def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n in (0, 1):
            return n
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return b

    def get_nth_fibonacci_divisible_by_four(n):
        idx, value = (2, fibonacci(n))
        while value % 4:
            idx += 1
            value = fibonacci(idx)
        return idx
    fibonacci_index = get_nth_fibonacci_divisible_by_four(fibonacci(len(binary_string)))
    return int(binary_string, 2) % fibonacci_index == 0