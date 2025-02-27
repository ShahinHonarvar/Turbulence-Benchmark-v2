def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_174th_num = 15352872971775258597330604823173345468743531868615127124959630487510449860
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_174th_num == 0