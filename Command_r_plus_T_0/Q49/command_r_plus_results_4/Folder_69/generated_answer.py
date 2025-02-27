def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_170th_number = 1907556594923609040929194974751705220777112677004504199784112923456715332
    binary_decimal = int(binary_str, 2)
    return binary_decimal % fib_170th_number == 0