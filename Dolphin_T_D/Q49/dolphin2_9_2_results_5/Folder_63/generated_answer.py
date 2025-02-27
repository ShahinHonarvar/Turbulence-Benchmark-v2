def if_decimal_is_divisible(binary_representation):
    n = int(binary_representation, 2)

    def compute_fib(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for i in range(2, n + 1):
                a, b = (b, a + b)
            return b
    fib_number = compute_fib(144)
    return n % fib_number == 0