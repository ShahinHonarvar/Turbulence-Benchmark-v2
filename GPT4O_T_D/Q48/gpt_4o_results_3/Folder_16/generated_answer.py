def return_binary_or_hexa(t):
    a = t[90]
    b = t[97]
    missing_numbers_sum = sum((i for i in range(a + 1, b) if i not in t[91:98]))
    if missing_numbers_sum == 0:
        return ''
    if missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]