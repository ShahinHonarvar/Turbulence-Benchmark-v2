def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < 68:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    if fibonacci_numbers[67] != 0 and decimal % fibonacci_numbers[67] == 0:
        return True
    else:
        return False