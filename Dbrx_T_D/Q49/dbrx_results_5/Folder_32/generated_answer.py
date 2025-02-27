def if_decimal_is_divisible(bin_repr: str) -> bool:
    decimal_num = int(bin_repr, 2)
    fib_178 = next(islice(fibonacci(), 178 - 1, 178 - 1))
    return decimal_num % fib_178 == 0

def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)