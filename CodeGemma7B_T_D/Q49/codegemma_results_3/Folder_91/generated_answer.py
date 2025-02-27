def if_decimal_is_divisible(binary_representation):
    fib = [0, 1]
    index = 0
    current_number = int(binary_representation, 2)
    while current_number > 0:
        if current_number == fib[index]:
            return True
        next_term = fib[index] + fib[index + 1]
        fib.append(next_term)
        index += 1
        current_number -= next_term
    return False