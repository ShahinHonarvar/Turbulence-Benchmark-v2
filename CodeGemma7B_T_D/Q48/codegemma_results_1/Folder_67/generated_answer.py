def return_binary_or_hexa(tup, a, b):
    sum = 0
    for num in range(a + 1, b):
        if num not in tup[44:68]:
            sum += num
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()