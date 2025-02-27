def if_decimal_is_divisible(binary):

    def Fibonacci_number(n):
        if n in (0, 1):
            return n
        first, second = (0, 1)
        for i in range(1, n):
            first, second = (second, first + second)
        return second
    nth = Fibonacci_number(19)
    decimal = 0
    for digit in reversed(binary):
        decimal += int(digit) * nth
        nth //= 2
    return not decimal % nth