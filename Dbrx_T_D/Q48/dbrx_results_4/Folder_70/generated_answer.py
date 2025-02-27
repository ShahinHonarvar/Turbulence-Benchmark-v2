def return_binary_or_hexa(sorted_tuple):
    a = sorted_tuple[42]
    b = sorted_tuple[69]
    sum = 0
    for i in range(a + 1, b):
        if i not in sorted_tuple[43:70]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()