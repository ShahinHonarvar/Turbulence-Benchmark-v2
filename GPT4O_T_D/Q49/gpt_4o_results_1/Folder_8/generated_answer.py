def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    for i in range(2, 55):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    fib_54 = fibonacci[54]
    decimal = int(binary_str, 2)
    return decimal % fib_54 == 0