def if_decimal_is_divisible(binary_str):

    def fibonacci_iter():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)
    fibonacci_num = next((f for f in fibonacci_iter() if f >= int(binary_str, 2)))
    return fibonacci_num % 69 == 0