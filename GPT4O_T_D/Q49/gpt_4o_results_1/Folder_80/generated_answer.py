def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    for i in range(2, 180):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    fibonacci_179 = fibonacci[179]
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_179 == 0