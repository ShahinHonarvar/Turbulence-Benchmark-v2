def return_binary_or_hexa(t):
    a, b = (t[10], t[12])
    present_sum = sum(t[11:13])
    all_sum = sum(range(a + 1, b))
    missing_sum = all_sum - present_sum
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]