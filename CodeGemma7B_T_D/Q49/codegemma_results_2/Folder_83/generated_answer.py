def if_decimal_is_divisible(binary_representation_str: str) -> bool:

    def fibonacci(value):
        if value in (0, 1):
            return 1
        else:
            return fibonacci(value - 1) + fibonacci(value - 2)
    value_from_bin = int(binary_representation_str, 2)
    if fibonacci(60) % value_from_bin == 0:
        return True
    else:
        return False