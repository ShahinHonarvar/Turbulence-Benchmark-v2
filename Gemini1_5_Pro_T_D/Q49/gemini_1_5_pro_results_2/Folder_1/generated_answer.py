def if_decimal_is_divisible(binary_representation):
    fibonacci_numbers = [0, 1]
    for i in range(2, 90):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    decimal_representation = 0
    for digit in range(len(binary_representation)):
        if binary_representation[digit] == '1':
            decimal_representation += 2 ** (len(binary_representation) - digit - 1)
    if decimal_representation % fibonacci_numbers[89] == 0:
        return True
    else:
        return False