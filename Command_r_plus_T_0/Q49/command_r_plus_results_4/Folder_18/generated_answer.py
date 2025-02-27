def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_199th = 199426992575100915116168329271913112129525568
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_199th == 0