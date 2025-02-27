def get_next_fibonacci(entry):
    if entry == 0:
        return 1
    elif entry == 1:
        return 1
    else:
        return get_next_fibonacci(entry - 1) + get_next_fibonacci(entry - 2)

def get_fibonacci(entry):
    result_list = []
    for number in range(entry + 1):
        result_list.append(get_next_fibonacci(number))
    return result_list[entry]

def get_int_by_binary(entry):
    multiplier = len(entry) - 1
    result = 0
    for digit in entry:
        digit = int(digit)
        result += multiplier * digit
        multiplier -= 1
    return result

def if_decimal_is_divisible(binary):
    binary = binary[::-1]
    number = get_int_by_binary(binary)
    fibonacci_list = get_fibonacci(76)
    for fibonacci in fibonacci_list:
        if fibonacci % number == 0:
            return True
    return False