def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_118th_number = 1929369125569193047509971724720374423964548739301387494821937076754725179174545372706
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_118th_number == 0