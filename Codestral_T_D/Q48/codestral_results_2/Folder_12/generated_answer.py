def return_binary_or_hexa(t):
    a = t[16]
    b = t[87]
    missing_nums = set(range(a + 1, b)) - set(t[16:87])
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]