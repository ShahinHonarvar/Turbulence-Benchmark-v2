def if_decimal_is_divisible(binary):

    def fib_up_to(n):
        for k, F in enumerate(Fibonacci()):
            if k > n:
                break
            yield F
    a, b = (0, 1)
    for digit in map(int, reversed(binary)):
        a, b = (b, a + b)
        if a % 180 == 0:
            return True
    return False

def Fibonacci():
    yield 0
    a, b = (0, 1)
    while True:
        a, b = (b, a + b)
        yield b