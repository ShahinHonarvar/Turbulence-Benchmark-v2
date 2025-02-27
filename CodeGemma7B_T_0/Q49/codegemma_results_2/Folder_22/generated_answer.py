def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    decimal = int(binary_representation, 2)
    for i in range(20):
        if decimal % fibonacci(i) == 0:
            return True
    return False