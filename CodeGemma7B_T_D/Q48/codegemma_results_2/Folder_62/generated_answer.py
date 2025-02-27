def return_binary_or_hexa(tup):
    a, b = (tup[50], tup[92])
    low = a + 1
    high = b - 1
    sum = 0
    for num in range(low, high + 1):
        if num not in tup[50:93]:
            sum += num
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()