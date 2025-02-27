def create_fibonacci(n):
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci_13 = fibonacci[13]
    if fibonacci_13 == 0:
        create_fibonacci(fibonacci_13 + 10)
    return fibonacci_13 != 0 and decimal % fibonacci[13] == 0