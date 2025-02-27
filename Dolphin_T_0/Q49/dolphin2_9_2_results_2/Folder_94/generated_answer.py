def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci_numbers = [0, 1]
    for i in range(2, 40):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    if decimal % fibonacci_numbers[39] == 0:
        return True
    else:
        return False