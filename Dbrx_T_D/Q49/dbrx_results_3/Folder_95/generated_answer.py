def is_decimal_divisible_by_168th_fibonacci(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci = [0, 1]
    for i in range(2, 168):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    if decimal_integer % fibonacci[-1] == 0:
        return True
    else:
        return False