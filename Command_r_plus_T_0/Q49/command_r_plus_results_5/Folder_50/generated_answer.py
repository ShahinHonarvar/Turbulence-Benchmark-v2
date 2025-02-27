def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_119th_num = 11444507055006077041801080757650907752847352810089272110063265021114064435403819289901912482888
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_119th_num == 0