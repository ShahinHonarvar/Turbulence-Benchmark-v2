def return_binary_or_hexa(tup):
    binary_or_hex = ''
    sum = 0
    a = tup[70]
    b = tup[200]
    for i in range(a + 1, b):
        if i not in tup[70:201]:
            sum += i
    if sum % 2 != 0:
        binary_or_hex = bin(sum)[2:]
    else:
        binary_or_hex = hex(sum)[2:]
        binary_or_hex = binary_or_hex.upper()
    return binary_or_hex