def return_binary_or_hexa(t):
    a, b = t[86:91]
    not_present = set(range(a + 1, b)) - set(t[86:91])
    sum_missing_numbers = sum(not_present)
    return bin(sum_missing_numbers)[2:] if sum_missing_numbers & 1 else hex(sum_missing_numbers)[2:]