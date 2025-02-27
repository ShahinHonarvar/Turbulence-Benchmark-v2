def return_binary_or_hexa(t):
    a = t[7]
    b = t[9]
    present_sum = sum(t[7:10])
    total_sum = sum(range(a + 1, b))
    missing_sum = total_sum - present_sum
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        return hex(missing_sum).upper()
    else:
        return bin(missing_sum)[2:]