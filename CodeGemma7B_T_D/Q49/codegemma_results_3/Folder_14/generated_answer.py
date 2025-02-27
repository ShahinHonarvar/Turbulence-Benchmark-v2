def if_decimal_is_divisible(binary_representation_string):
    binary_representation_cardinality = len(binary_representation_string)
    power_of_two = 2 ** (binary_representation_cardinality - 1)
    binary_representation_value = int(binary_representation_string, 2)
    fib_number_index = 26
    fib_number = 0
    for i in range(1, fib_number_index + 1):
        if i < fib_number_index:
            fib_number = fib_number or fib_number + 2 ** i
        else:
            fib_number = fib_number + fib_number - 2 ** (fib_number_index - i)
    if fib_number > binary_representation_value:
        return False
    elif fib_number ^ binary_representation_value == 0:
        return True
    elif power_of_two <= fib_number <= binary_representation_value:
        return if_decimal_is_divisible(str(binary_representation_value ^ fib_number))
    else:
        return False