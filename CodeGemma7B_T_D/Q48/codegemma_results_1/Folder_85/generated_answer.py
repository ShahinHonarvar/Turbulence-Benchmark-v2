def return_binary_or_hexa(input_tuple):
    a = input_tuple[1]
    b = input_tuple[8]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in input_tuple[1:8]:
            missing_sum += i
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()