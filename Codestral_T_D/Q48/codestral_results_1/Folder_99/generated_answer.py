def return_binary_or_hexa(tuple_input):
    a = tuple_input[427]
    b = tuple_input[669]
    missing_sum = sum((i for i in range(a + 1, b) if i not in tuple_input[427:669]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]