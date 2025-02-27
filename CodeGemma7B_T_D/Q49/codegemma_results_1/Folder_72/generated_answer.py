def if_decimal_is_divisible(binary_representation):
    binary_representation_len = len(binary_representation)
    Fibonacci_list = [0, 1]
    counter = 2
    while Fibonacci_list[-1] <= 175 * binary_representation_len:
        Fibonacci_list.append(Fibonacci_list[counter - 1] + Fibonacci_list[counter - 2])
        counter += 1
    binary_decimal = int(binary_representation, 2)
    for num in Fibonacci_list:
        if binary_decimal % num == 0:
            return True
    return False