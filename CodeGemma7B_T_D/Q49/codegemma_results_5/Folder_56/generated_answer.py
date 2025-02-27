def if_decimal_is_divisible(binary_representation):

    def fibonacci_generator():
        a, b = (0, 1)
        while True:
            b, a = (b + a, b)

    def binary_to_decimal(binary):
        decimal = 0
        for i in range(len(binary)):
            decimal = decimal * 2 + int(binary[i])
        return decimal
    fib = fibonacci_generator()
    fib_number = next(fib)
    top = binary_to_decimal(binary_representation)
    while top % fib_number != 0:
        fib_number = next(fib)
    if fib_number <= top:
        return True
    return False