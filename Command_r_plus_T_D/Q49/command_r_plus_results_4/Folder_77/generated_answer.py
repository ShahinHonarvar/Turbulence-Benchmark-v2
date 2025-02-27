def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_110th = 31941592653589793238295246821408311189542052640
    binary_int = int(binary_str, 2)
    if binary_int % fib_110th == 0:
        return True
    else:
        return False