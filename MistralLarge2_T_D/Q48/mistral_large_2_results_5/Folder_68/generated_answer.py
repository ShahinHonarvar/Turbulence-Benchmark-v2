def return_binary_or_hexa(input_tuple):
    a, b = (input_tuple[0], input_tuple[9])
    missing_sum = sum((i for i in range(a + 1, b) if i not in input_tuple))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]