def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fibonacci_126 = 31128691495616592375927767145016217682111371
    return decimal_num % fibonacci_126 == 0