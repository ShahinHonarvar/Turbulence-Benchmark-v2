def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_nums = [0, 1]
    while fibonacci_nums[-1] + fibonacci_nums[-2] < decimal_integer:
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
    if decimal_integer % fibonacci_nums[-138] == 0:
        return True
    else:
        return False