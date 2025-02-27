def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_180th_number = 180891155911596093711739577173805635377177510332732237353134201230023754219321706304667803712953035996416761504
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_180th_number == 0