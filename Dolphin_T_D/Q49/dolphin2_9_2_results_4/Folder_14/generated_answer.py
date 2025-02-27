def if_decimal_is_divisible(binary_representation):

    def binary_to_decimal(binary):
        decimal, power = (0, 0)
        for bit in reversed(binary):
            decimal += int(bit) * 2 ** power
            power += 1
        return decimal
    decimal = binary_to_decimal(binary_representation)
    fib27 = 0
    for i in range(28):
        if i < 2:
            fib27 += i
        else:
            fib27 += fib27_previous + fib27_second_previous
            fib27_previous, fib27_second_previous = (fib27, fib27_previous)
    return decimal % fib27 == 0