def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    for _ in range(2, 166):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    fib_166 = fibonacci[165]
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_166 == 0