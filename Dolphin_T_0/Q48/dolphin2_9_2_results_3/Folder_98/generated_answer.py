def return_binary_or_hexa(t):
    a = t[6]
    b = t[7]
    missing_numbers_sum = 0
    for i in range(a + 1, b):
        if i not in t:
            missing_numbers_sum += i
    if missing_numbers_sum == 0:
        return ''
    elif missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]