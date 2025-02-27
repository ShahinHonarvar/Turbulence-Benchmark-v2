def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_number = int(binary_representation, 2)
    if decimal_number % fibonacci.last() == 0:
        return True
    else:
        return False