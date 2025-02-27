def return_binary_or_hexa(t):
    a = t[110]
    b = t[348]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in t[110:349]:
            missing_sum += num
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()