def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_187 = 1845493206761068465016531494448
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_187 == 0