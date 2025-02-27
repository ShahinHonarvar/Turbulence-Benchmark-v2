def if_decimal_is_divisible(binary_representation):

    def fibonacci(index):
        if index <= 1:
            return 1
        return fibonacci(index - 1) + fibonacci(index - 2)
    decimal = int(binary_representation, 2)
    fibonacci_list = [fibonacci(i) for i in range(185)]
    return decimal % fibonacci_list[184] == 0