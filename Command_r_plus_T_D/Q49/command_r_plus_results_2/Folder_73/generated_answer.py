def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_164th_number = 1378983229509324573191073684504670411559563470686246110247541194697748672
    binary_as_int = int(binary_str, 2)
    if binary_as_int % fib_164th_number == 0:
        return True
    else:
        return False