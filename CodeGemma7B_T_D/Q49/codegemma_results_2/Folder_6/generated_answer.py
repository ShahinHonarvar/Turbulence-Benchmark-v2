def if_decimal_is_divisible(binary_str):

    def get_next_fibonacci(a, b):
        return a + b
    b = 1
    a = 0
    fib_num = 0
    for digit in binary_str:
        fib_num *= 2
        fib_num += int(digit)
    for i in range(184):
        a, b = (b, get_next_fibonacci(a, b))
    return fib_num % b == 0