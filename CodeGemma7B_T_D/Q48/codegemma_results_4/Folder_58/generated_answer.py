def return_binary_or_hexa(tuple1):
    a = tuple1[275]
    b = tuple1[871]
    xor_sum = 0
    for num in range(a + 1, b):
        if num not in tuple1[275:872]:
            xor_sum ^= num
    if xor_sum % 2 == 0:
        return hex(xor_sum)[2:]
    else:
        return bin(xor_sum)[2:]