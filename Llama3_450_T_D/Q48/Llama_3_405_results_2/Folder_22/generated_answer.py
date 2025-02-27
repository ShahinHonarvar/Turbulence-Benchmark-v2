def return_binary_or_hexa(t):
    a = t[40]
    b = t[200]
    full_set = set(range(a + 1, b))
    given_set = set(t[41:200])
    missing_nums = full_set - given_set
    total_sum = sum(missing_nums)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]