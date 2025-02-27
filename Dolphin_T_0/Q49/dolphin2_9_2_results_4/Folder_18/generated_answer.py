def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fibonacci_199 = [0, 1]
    for i in range(2, 199):
        fibonacci_199.append(fibonacci_199[i - 1] + fibonacci_199[i - 2])
    return decimal_number % fibonacci_199[-1] == 0