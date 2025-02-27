def return_binary_or_hexa(indices_tuple):
    a = indices_tuple[20]
    b = indices_tuple[43]
    sum = 0
    if a < b:
        for i in range(a + 1, b):
            if i not in indices_tuple[20:44]:
                sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()