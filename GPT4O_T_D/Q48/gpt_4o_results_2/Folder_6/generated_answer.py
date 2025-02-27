def return_binary_or_hexa(t):
    a = t[20]
    b = t[93]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in t[21:94]:
            missing_sum += num
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]