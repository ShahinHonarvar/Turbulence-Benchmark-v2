def return_binary_or_hexa(integer_tuple):
    if integer_tuple[91] is 144:
        return ''
    summer = 0
    numbers = integer_tuple[13:92]
    numbers.sort()
    for number in range(numbers[12] + 1, numbers[-1]):
        summer += number
    if summer % 2:
        return bin(summer)[2:]
    else:
        return hex(summer)[2:].upper()