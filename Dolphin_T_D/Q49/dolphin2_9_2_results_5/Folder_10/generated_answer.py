def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fibonacci_series = [0, 1]
    for i in range(2, 89):
        fibonacci_series.append(fibonacci_series[i - 1] + fibonacci_series[i - 2])
    return decimal_number % fibonacci_series[88] == 0