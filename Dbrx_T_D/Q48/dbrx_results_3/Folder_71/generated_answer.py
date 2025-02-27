def return_binary_or_hexa(tupl):
    a = tupl[20]
    b = tupl[35]
    existing = set(tupl[20:36])
    sum = 0
    for i in range(a + 1, b):
        if i not in existing:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:].replace('b', '')