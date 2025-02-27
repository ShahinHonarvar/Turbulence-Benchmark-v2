def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[0], int_tuple[9])
    sum = 0
    present_set = set(int_tuple[1:9])
    for num in range(a + 1, b):
        if num not in present_set:
            sum += num
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]