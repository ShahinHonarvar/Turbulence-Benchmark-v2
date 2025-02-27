def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_178th_number = 151222158635774125738631045315033607488
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fib_178th_number == 0