def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_154th = 45180769394496674882313098192740709841447971639877558044737582788790510339042012773355336318367
    binary_int = int(binary_str, 2)
    return binary_int % fib_154th == 0