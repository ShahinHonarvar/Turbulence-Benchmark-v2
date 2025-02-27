def if_decimal_is_divisible(binary_rep):

    def fibonacci_seq(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci_seq(n - 1) + fibonacci_seq(n - 2)
    index = 125
    fibo = fibonacci_seq(index)
    decimal = int(binary_rep, 2)
    if decimal % fibo == 0:
        return True
    else:
        return False