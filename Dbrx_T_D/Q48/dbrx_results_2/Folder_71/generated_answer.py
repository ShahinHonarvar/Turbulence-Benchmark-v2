def return_binary_or_hexa(input_tuple):
    a = input_tuple[20]
    b = input_tuple[35]
    sum = 0
    for i in range(a + 1, b):
        if input_tuple[20:36].count(i) == 0:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()