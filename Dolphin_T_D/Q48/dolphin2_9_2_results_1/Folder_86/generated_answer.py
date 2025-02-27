def return_binary_or_hexa(tuples):
    a = tuples[19]
    b = tuples[32]
    sum = 0
    present_set = set(tuples[20:32])
    for i in range(a + 1, b):
        if i not in present_set:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()
    return ''