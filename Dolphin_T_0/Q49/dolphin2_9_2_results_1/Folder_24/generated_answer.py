def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = [0, 1]
    for i in range(2, 56):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    n = fibonacci[-1]
    if decimal % n == 0:
        return True
    else:
        return False