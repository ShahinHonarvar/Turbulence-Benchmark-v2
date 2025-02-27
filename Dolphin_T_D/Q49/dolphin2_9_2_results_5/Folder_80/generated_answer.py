def if_decimal_is_divisible(binary_rep):
    index = 179

    def compute_fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(n - 1):
                a, b = (b, a + b)
            return b

    def binary_to_int(binary_rep):
        return int(binary_rep, 2)
    fibonacci = compute_fibonacci(index)
    decimal = binary_to_int(binary_rep)
    return decimal % fibonacci == 0