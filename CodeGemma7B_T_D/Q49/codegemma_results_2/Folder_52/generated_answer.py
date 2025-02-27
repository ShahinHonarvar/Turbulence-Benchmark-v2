def if_decimal_is_divisible(binary_representation):
    fibonacci_series = [0, 1]
    for i in range(2, 1000):
        fibonacci_series.append(fibonacci_series[i - 2] + fibonacci_series[i - 1])
    binary_to_decimal = int(binary_representation, 2)
    return binary_to_decimal % fibonacci_series[176] == 0