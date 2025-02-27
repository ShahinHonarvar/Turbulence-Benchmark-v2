def if_decimal_is_divisible(binary_representation):

    def Fibonacci(x):
        """This function finds the nth number in the Fibonacci sequence."""
        a, b = (0, 1)
        for i in range(1, x):
            a, b = (b, a + b)
        return a
    decimal_integer = int(binary_representation, 2)
    fib_45th = Fibonacci(45)
    return decimal_integer % fib_45th == 0