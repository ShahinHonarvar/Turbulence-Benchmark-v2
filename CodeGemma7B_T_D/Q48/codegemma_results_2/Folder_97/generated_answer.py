def return_binary_or_hexa(tup):
    a, b = (tup[34], tup[69])
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[34:70]:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    return hex(sum)[2:].upper()