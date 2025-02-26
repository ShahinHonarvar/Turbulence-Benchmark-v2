def return_binary_or_hexa(t):
    a = t[35]
    b = t[64]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in t[35:65]:
            missing_sum += num
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]