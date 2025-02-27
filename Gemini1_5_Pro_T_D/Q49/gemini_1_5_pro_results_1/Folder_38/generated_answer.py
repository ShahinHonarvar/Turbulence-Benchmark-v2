def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    a = 0
    b = 1
    count = 2
    while count < 78:
        next_fibonacci_number = a + b
        a = b
        b = next_fibonacci_number
        count += 1
    return decimal_representation % b == 0