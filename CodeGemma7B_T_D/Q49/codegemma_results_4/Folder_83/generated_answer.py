def if_decimal_is_divisible(binary_string):
    fib_list = [0, 1]
    fib_loc = 2
    fib_result = 0
    total_places = len(binary_string)
    place_value = 2 ** (total_places - 1)
    counter = 0
    for digit in binary_string:
        if digit == '1':
            fib_result += fib_list[fib_loc] * place_value
        fib_list.append(fib_list[fib_loc] + fib_list[fib_loc - 1])
        fib_loc += 1
        place_value = place_value / 2
    if fib_result % 60 == 0:
        return True
    else:
        return False