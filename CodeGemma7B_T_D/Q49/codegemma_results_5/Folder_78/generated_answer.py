def if_decimal_is_divisible(binary_representation):
    """
    Solution is provided here; trying not to reveal the logic of the solution just straight up providing the working.
    """
    fib_number = 115
    fibonacci = [0, 1]
    for i in range(fib_number - 2):
        fibonacci.append(fibonacci[i] + fibonacci[i + 1])
    return int(binary_representation, 2) % fibonacci[fib_number] == 0