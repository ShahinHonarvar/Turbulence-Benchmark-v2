def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    n = 154
    fibonacci_numbers = [0, 1]
    for i in range(2, n + 1):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    return decimal % fibonacci_numbers[n - 1] == 0