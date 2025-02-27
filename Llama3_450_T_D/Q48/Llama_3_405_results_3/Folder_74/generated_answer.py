def return_binary_or_hexa(t):
    a = t[69]
    b = t[97]
    total_sum = sum(range(a + 1, b))
    present_sum = sum((i for i in t[70:97] if a < i < b))
    diff_sum = total_sum - present_sum
    if diff_sum == 0:
        return ''
    elif diff_sum % 2:
        return bin(diff_sum)[2:]
    else:
        return hex(diff_sum)[2:]