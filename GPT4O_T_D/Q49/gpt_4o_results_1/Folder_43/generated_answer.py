def if_decimal_is_divisible(binary_str):
    fib77 = 5527939700884757
    decimal_number = int(binary_str, 2)
    return decimal_number % fib77 == 0