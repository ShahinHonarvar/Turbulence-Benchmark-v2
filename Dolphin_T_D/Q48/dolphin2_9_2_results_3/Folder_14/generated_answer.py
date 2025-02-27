def return_binary_or_hexa(t):
    a = t[2]
    b = t[5]
    total_sum = sum(range(a + 1, b))
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in t[2:6]:
            missing_sum += i
    if missing_sum == total_sum:
        return ''
    elif missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]