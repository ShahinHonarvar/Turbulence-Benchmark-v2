def return_binary_or_hexa(t):
    a = t[10]
    b = t[28]
    existing_numbers = set(t[10:29])
    missing_sum = sum((num for num in range(a + 1, b) if num not in existing_numbers))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]