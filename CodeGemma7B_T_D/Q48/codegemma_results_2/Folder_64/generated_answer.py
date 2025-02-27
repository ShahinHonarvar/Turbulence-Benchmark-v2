def return_binary_or_hexa(sorted_tuple):
    a, _, _, _, _, b = sorted_tuple
    sum = 0
    for i in range(a + 1, b):
        if i not in sorted_tuple:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    return hex(sum)[2:].upper() if sum else ''