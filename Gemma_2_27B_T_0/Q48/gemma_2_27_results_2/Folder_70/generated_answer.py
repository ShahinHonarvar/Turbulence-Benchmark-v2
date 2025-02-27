def return_binary_or_hexa(data):
    a = data[43]
    b = data[70]
    total = 0
    for i in range(a + 1, b):
        if i not in data[43:70]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]