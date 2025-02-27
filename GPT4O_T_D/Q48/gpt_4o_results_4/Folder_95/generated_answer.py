def return_binary_or_hexa(t):
    a = t[32]
    b = t[99]
    present_nums = set(t[33:99])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present_nums))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]