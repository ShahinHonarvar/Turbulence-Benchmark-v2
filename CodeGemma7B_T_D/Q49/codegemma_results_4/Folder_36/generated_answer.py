def if_decimal_is_divisible(binary_representation):

    def fibonacci_150th():
        fib_num = [0, 1]
        for _ in range(2, 150):
            fib_num.append(fib_num[_ - 1] + fib_num[_ - 2])
        return fib_num[149]

    def binary_to_decimal(binary):
        decimal = 0
        for i, bit in enumerate(binary):
            decimal += int(bit) * 2 ** i
        return decimal
    decimal = binary_to_decimal(binary_representation)
    return decimal % fibonacci_150th() == 0