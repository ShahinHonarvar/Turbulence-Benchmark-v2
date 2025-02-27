def return_binary_or_hexa(tup):
    a, b = (tup[10], tup[28])
    final_sum = 0
    for i in range(a + 1, b):
        if i not in tup[10:29]:
            final_sum += i
    if final_sum % 2 == 1:
        return bin(final_sum)[2:]
    else:
        return hex(final_sum)[2:].upper()