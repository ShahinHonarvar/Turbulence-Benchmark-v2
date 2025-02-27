def if_decimal_is_divisible(binary_representation):
    binary_representation = str(binary_representation)
    fib_numbers = [0, 1]
    for number in range(2, 1000):
        fib_numbers.append(fib_numbers[number - 2] + fib_numbers[number - 1])
    index = 0
    for number in fib_numbers:
        if number == int(binary_representation, 2):
            break
        index += 1
    if index % 4 == 0:
        return True
    else:
        return False