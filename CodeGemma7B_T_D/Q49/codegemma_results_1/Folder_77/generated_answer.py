def if_decimal_is_divisible(binary_representation):
    previous_number = 0
    current_number = 1
    fib_index = 0
    found_it = False
    while not found_it:
        fib_number = previous_number + current_number
        binary_fib_number = bin(fib_number)[2:]
        if len(binary_fib_number) > len(binary_representation):
            found_it = True
        elif binary_fib_number == binary_representation[:len(binary_fib_number)]:
            multiple = int(binary_representation[len(binary_fib_number):], 2)
            if multiple == 0 or binary_representation[0] == '1':
                found_it = True
            else:
                previous_number = current_number
                current_number = fib_number
                fib_index += 1
    if found_it and fib_index % 110 == 0:
        return True
    else:
        return False