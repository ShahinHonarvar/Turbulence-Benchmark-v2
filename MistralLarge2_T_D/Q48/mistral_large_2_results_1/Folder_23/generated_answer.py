def return_binary_or_hexa(t):
    a = t[20]
    b = t[36]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in t[20:37]:
            missing_sum += i
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]