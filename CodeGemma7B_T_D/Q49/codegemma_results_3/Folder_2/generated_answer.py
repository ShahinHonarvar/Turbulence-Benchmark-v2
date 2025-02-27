from math import floor

def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def binary_to_decimal(binary):
        decimal = 0
        n = 0
        for bit in reversed(binary):
            decimal += int(bit) * 2 ** n
            n += 1
        return decimal
    fib_list = []
    for n in range(0, 999):
        fib_list.append(fibonacci(n))
    multiple_of_125 = floor(fib_list[999] / 125) * 125
    if binary_to_decimal(binary) % multiple_of_125 == 0:
        return True
    else:
        return False