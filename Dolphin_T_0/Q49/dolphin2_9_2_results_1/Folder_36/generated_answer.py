def if_decimal_is_divisible(binary_string):

    def bin_to_dec(binary_string):
        result = 0
        for char in binary_string:
            result = result * 2 + int(char)
        return result

    def fibonacci(n):
        if n <= 1:
            return n
        else:
            a, b = (0, 1)
            for _ in range(2, n + 1):
                a, b = (b, a + b)
            return b
    return bin_to_dec(binary_string) % fibonacci(150) == 0