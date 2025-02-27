def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_175th_num = 13789832983133431374651075142883639821325433
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_175th_num == 0