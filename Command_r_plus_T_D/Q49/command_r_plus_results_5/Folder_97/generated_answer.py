def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_114th_num = 1845493206761195609275104010748722359176569371350331719035703476455942913142324870181631186273127
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_114th_num == 0