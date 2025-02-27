def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fibonacci_199 = [0, 1]
    while len(fibonacci_199) < 199:
        fibonacci_199.append(fibonacci_199[-1] + fibonacci_199[-2])
    if decimal_number % fibonacci_199[198] == 0:
        return True
    else:
        return False