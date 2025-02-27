def return_binary_or_hexa(t):
    a = t[13]
    b = t[70]
    sum = 0
    present = set()
    for i in range(a + 1, b):
        present.add(i)
    for i in range(a + 1, b):
        if i not in present:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()