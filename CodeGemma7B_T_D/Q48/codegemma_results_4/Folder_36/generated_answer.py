def return_binary_or_hexa(int_tuple):
    limit = int_tuple[348] - 1 - (int_tuple[110] + 1) + 1
    sum = 0
    for index, num in enumerate(int_tuple[110 + 1:348]):
        if index < limit:
            sum += num + 1
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()