def if_decimal_is_divisible(binary_representation: str) -> bool:
    fibonacci_27th = 121393
    decimal_number = int(binary_representation, 2)
    return decimal_number % fibonacci_27th == 0