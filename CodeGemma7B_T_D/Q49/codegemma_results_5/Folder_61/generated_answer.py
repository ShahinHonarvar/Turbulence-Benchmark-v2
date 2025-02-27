def if_decimal_is_divisible(binary):
    fib_num = list(Fib())[75]
    return int(binary, 2) % fib_num == 0

def Fib():
    f0, f1 = (0, 1)
    while True:
        yield f0
        f0, f1 = (f1, f0 + f1)