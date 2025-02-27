def if_decimal_is_divisible(binary_str):

    def generate_fibonacci():
        a, b = (0, 1)
        for _ in range(20):
            yield a
            a, b = (b, a + b)
    decimal = int(binary_str, 2)
    fib_19 = list(generate_fibonacci())[-1]
    return decimal % fib_19 == 0