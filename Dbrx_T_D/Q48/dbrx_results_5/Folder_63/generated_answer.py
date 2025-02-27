def return_binary_or_hexa(input_tuple):
    if input_tuple[85] - input_tuple[80] < 3:
        return ''
    sum = 0
    for i in range(input_tuple[80] + 1, input_tuple[85]):
        if i not in input_tuple:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()