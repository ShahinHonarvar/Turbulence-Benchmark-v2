def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci = [0, 1]
    for i in range(2, 24):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    divisor = fibonacci[23]
    if decimal % divisor == 0:
        return True
    else:
        return False