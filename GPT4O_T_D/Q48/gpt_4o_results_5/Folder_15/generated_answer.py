def return_binary_or_hexa(t):
    a = t[0]
    b = t[4]
    missing_sum = sum((num for num in range(a + 1, b) if num not in t[1:4]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]