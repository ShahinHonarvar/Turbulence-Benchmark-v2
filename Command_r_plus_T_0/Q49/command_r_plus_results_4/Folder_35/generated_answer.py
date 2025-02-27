def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_187th = 180355563295578060245942140964671102020643593021216
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_187th == 0