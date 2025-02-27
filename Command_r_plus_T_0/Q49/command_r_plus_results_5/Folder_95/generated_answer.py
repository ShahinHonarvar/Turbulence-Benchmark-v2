def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_168 = 1688010428570229976774800718556505616620966695314741107752402411571732036930449
    decimal = int(binary_str, 2)
    return decimal % fib_168 == 0