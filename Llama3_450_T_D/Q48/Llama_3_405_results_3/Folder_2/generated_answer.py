def return_binary_or_hexa(t):
    a = t[72]
    b = t[93]
    total_sum = sum(range(a + 1, b))
    existing_sum = sum((i for i in t[73:93] if a < i < b))
    diff_sum = total_sum - existing_sum
    if diff_sum == 0:
        return ''
    elif diff_sum % 2 != 0:
        return bin(diff_sum)[2:]
    else:
        return hex(diff_sum)[2:]