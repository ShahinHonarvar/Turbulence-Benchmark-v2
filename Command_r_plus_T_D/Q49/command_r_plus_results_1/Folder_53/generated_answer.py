def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_64th_number = 18456329761298930358157937939371715393
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_64th_number == 0