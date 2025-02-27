def if_decimal_is_divisible(bin_str):
    decimal_number = int(bin_str, 2)
    fibonacci_20 = [0, 1]
    for i in range(2, 20):
        fibonacci_20.append(fibonacci_20[i - 1] + fibonacci_20[i - 2])
    if decimal_number % fibonacci_20[19] == 0:
        return True
    else:
        return False