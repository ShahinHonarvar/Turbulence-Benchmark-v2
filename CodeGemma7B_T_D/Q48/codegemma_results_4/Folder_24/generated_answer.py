def return_binary_or_hexa(tup):
    a, b = (tup[13], tup[91])
    sum = 0
    for num in range(a + 1, b):
        if num not in tup[13:92]:
            sum += num
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()