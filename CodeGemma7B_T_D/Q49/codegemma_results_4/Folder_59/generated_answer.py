def if_decimal_is_divisible(binary_representation):
    current_number = int(binary_representation, 2)
    fib_index = 0
    fib_array = []
    fib_array.append(0)
    while current_number > 0:
        fib_index += 1
        fib_array.append(fib_array[fib_index - 1] + fib_array[fib_index - 2])
        if current_number % fib_array[fib_index - 1] == 0:
            return True
        current_number -= fib_array[fib_index - 1]
    return False