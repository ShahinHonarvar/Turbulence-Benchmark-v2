def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_160th_number = 222668772620387150327437195432353081631900925177
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fib_160th_number == 0