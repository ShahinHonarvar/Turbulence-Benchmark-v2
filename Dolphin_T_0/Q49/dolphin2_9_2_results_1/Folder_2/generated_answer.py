def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    fibonacci_125 = [0, 1]
    for i in range(2, 125):
        fibonacci_125.append(fibonacci_125[i - 1] + fibonacci_125[i - 2])
    if n % fibonacci_125[-1] == 0:
        return True
    else:
        return False