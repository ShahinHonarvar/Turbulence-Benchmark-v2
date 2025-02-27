def return_binary_or_hexa(tuple_int):
    sum = 0
    for i in range(87, len(tuple_int)):
        if tuple_int[i] not in range(tuple_int[86] + 1, tuple_int[89]):
            sum += tuple_int[i]
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]