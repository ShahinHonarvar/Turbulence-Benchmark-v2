def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_134th = 193673245671163737246834657153960045713083809814527109722382596531422962371709340330891097699
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_134th == 0