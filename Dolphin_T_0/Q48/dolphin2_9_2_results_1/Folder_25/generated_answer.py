def return_binary_or_hexa(int_tuple):
    a = int(int_tuple[37])
    b = int(int_tuple[43])
    int_set = set(int_tuple)
    sum = 0
    for i in range(a + 1, b):
        if i not in int_set:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()