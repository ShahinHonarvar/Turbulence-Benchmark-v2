def if_decimal_is_divisible(binary_rep):

    def binary_to_decimal(binary_rep):
        return sum((int(binary_rep[i]) * 2 ** (len(binary_rep) - 1 - i) for i in range(len(binary_rep))))

    def fibonacci(n):
        a = 0
        b = 1
        while a < n:
            a, b = (b, a + b)
        return a
    fib_186 = fibonacci(186)
    decimal_rep = binary_to_decimal(binary_rep)
    if decimal_rep % fib_186 == 0:
        return True
    else:
        return False