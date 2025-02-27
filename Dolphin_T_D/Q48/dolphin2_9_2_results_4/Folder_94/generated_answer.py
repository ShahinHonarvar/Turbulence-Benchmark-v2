def return_binary_or_hexa(input_tuple):
    a = input_tuple[42]
    b = input_tuple[87]
    range_sum = sum(range(a + 1, b))
    present_sum = sum(input_tuple[42:88])
    difference = range_sum - present_sum
    if difference == 0:
        return ''
    elif difference % 2 == 1:
        return bin(difference)[2:]
    else:
        return hex(difference)[2:].upper()