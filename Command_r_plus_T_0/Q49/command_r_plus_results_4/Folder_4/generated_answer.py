def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_118th_number = 192936912556919304750997172472037442396454873930138749482193707675472517917454537832289171
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_118th_number == 0