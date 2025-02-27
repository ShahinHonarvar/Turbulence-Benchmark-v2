def return_binary_or_hexa(t):
    result = 0
    index = 0
    while index < len(t):
        if t[index] > 18:
            break
        index += 1
    for i in range(index + 1, len(t)):
        if i > 60:
            break
        if t[i] >= t[i - 1] + 2:
            result += t[i - 1] + 1
    if result & 1:
        return bin(result)[2:]
    else:
        return hex(result)[2:].upper()