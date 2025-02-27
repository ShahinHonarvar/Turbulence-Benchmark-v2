def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            x, y, z = (0, 0, fibonacci(n - 1))
            for i in range(2, n + 1):
                x, y, z = (y, y + x, z + y)
        return z
    decimal = 0
    for digit in reversed(binary_str):
        decimal = 2 * decimal + int(digit)
    for i in range(34, 51):
        if fibonacci(i) >= decimal:
            if fibonacci(i) % decimal == 0:
                return True
            else:
                return False