def return_binary_or_hexa(data):
    a = data[38]
    b = data[81]
    total = 0
    for i in range(a + 1, b):
        if i not in data[38:81]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    elif total == 0:
        return ''
    else:
        return hex(total)[2:]