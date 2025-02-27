def if_decimal_is_divisible(bin_repr):
    decimal_integer = int(bin_repr, 2)
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < 87:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return decimal_integer % fibonacci_numbers[86] == 0