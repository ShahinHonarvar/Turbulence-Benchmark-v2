def return_binary_or_hexa(tuple_input):
    a = tuple_input[20]
    b = tuple_input[93]
    missing_sum = sum((i for i in range(a + 1, b) if i not in tuple_input[20:94]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]