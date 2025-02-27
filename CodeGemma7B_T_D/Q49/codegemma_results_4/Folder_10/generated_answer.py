def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    binary_to_decimal = 0
    for i in range(len(binary_representation)):
        binary_to_decimal = binary_to_decimal + int(binary_representation[i]) * 2 ** (len(binary_representation) - 1 - i)
    binary_to_decimal = fibonacci(binary_to_decimal)
    if binary_to_decimal % fibonacci(88) == 0:
        return True
    else:
        return False