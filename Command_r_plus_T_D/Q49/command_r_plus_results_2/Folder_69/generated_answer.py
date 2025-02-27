def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_170th_number = 19089730604699811150871335373346102491690977185736786869219613674261108422451021642687
    binary_decimal = int(binary_str, 2)
    return binary_decimal % fib_170th_number == 0