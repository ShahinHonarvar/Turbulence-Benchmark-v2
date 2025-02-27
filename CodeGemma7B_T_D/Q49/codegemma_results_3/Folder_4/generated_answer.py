def if_decimal_is_divisible(binary_representation):
    fib_118th = fibonacci(118)
    decimal = int(binary_representation, 2)
    return decimal % fib_118th == 0

def fibonacci(k):
    if k <= 1:
        return k
    else:
        return fibonacci(k - 1) + fibonacci(k - 2)