def return_binary_or_hexa(data):
    a = data[50]
    b = data[92]
    total = sum([num for num in range(a + 1, b) if num not in data[50:92]])
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]