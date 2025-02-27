def if_decimal_is_divisible(binary_rep):

    def decimal_representation(binary_rep):
        return int(binary_rep, 2)

    def fibonacci(num):
        a, b = (0, 1)
        for _ in range(num):
            a, b = (b, a + b)
        return a
    decimal_num = decimal_representation(binary_rep)
    fib_num = fibonacci(20)
    return decimal_num % fib_num == 0