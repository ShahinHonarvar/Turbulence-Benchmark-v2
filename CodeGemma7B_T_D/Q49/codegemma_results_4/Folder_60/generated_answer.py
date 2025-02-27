def if_decimal_is_divisible(binary_string):

    def fibonacci_nums(num):
        a, b = (0, 1)
        for i in range(num):
            yield a
            a, b = (b, a + b)
    binary_value = int(binary_string, 2)
    for fib_num in fibonacci_nums(500):
        if fib_num == fibonacci_nums(108).next():
            return binary_value % fib_num == 0
    return False