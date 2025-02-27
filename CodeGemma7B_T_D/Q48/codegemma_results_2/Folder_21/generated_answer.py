def return_binary_or_hexa(tup):
    a = tup[15]
    b = tup[57]
    total_sum = sum([num for num in range(a + 1, b) if num not in tup[15:58]])
    if total_sum % 2:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:].upper()