def return_binary_or_hexa(t):
    a = t[20]
    b = t[36]
    numbers = set(t[21:36])
    sum = 0
    for num in range(a + 1, b):
        if num not in numbers:
            sum += num
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()