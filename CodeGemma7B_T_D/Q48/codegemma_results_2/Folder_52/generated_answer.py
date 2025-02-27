def return_binary_or_hexa(sorted_tuple):
    a, b = (sorted_tuple[38], sorted_tuple[81])
    sum = 0
    for i in range(a + 1, b):
        if i not in sorted_tuple[38:82]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()