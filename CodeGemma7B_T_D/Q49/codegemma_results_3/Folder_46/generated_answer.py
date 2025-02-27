def if_decimal_is_divisible(binary):
    """
            Is this supposed to be the Fibonacci sequence?
            """
    a, b = (0, 1)
    for _ in range(1, 1000):
        a, b = (b, a + b)
    c = int(binary, 2)
    if c % b == 0:
        return True
    return False