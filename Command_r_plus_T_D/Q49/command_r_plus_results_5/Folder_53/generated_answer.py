def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_64th_num = 1845493718930769065480396640016192016
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_64th_num == 0