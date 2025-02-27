def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_164 = 16640826216857328041329914927631369310776118888553255428152681713051448812351876617617211319930807427
    binary_int = int(binary_str, 2)
    return binary_int % fib_164 == 0