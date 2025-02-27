def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_154th_number = 29540796838835774569915673799744514768826259617100960464955616860129048052654046043065115069596029016
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_154th_number == 0